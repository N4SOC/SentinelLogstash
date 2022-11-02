from genericpath import isdir
import config
import yaml
import os
import subprocess

services = {}
args = {
    "environment_name": config.envName,
    "workspaceID": config.workspaceID,
    "workspaceKey": config.workspaceKey,
    "table": None
}

def deployids(interface,table) :
    volumes=['zeeklogs']
    yml = yaml.dump({"volumes": volumes})
    args["table"] = collector["table"]
    zeek={"build": {
                "context": "./zeek",
                "args": args
            },
                "image": "zeek_sentinel",
                "volumes":[]
            }
    zeek_ids=[]
    services['zeek']=zeek
    services['zeek_ids']=zeek_ids

    """
      zeek:
    build:
      context: ./zeek
      args:
        environment_name: ${environment_name}
        workspaceID: ${workspaceID}
        workspaceKey: ${workspaceKey}
    image: zeek_sentinel
    volumes:
      - type: volume
        source: zeeklogs
        target: /logs/
    profiles:
      - ids

  zeek_ids:
    build:
      context: ./zeek_ids
      args:
        span_interface: ${span_interface}
    image: zeek_ids
    volumes:
      - type: volume
        source: zeeklogs
        target: /opt/zeek/spool/zeek
    network_mode: host
    cap_add:
      - sys_nice
      - net_admin
    stdin_open: true # docker run -i
    tty: true # docker run -t
    profiles:
      - ids
      """

for collector in config.collectors:
    args["table"] = None
    if "table" in collector:  # If custom table is defined for collector
        args["table"] = collector["table"]
    if os.path.isdir(f"./{collector['name']}"):  # Confirm collector exists
        if collector['name'] == "ids":
            print("Audomtaed IDS deplotyment not yet available")
        else:
            if collector['proto'] == "tcp":
                ports = [f"{collector['port']}:514"]
            else:  # If syslog is UDP
                ports = [f"{collector['port']}:514/udp"]

            service = {"build": {
                "context": f"./{collector['name']}",
                "args": args
            },
                "image": f"{collector['name']}_sentinel",
                "ports": ports
            }
            services[collector['name']] = service
    else:
        print(f"Collector not found: {collector['name']}, please check configuration")
yml = yaml.dump({"services": services})

with open("docker-compose.yml", "w") as f:
    f.write(yml)

buildcmd = subprocess.run(["docker", "compose", "build"])
if buildcmd.returncode == 0:
    print(f"Build Successful - {len(services)} collectors built")
else:
    print("Build Failed")

runcmd = subprocess.run(["docker", "compose", "up", "-d"])
if runcmd.returncode == 0:
    print(f"Execution Successful - {len(services)} collectors running")
else:
    print("Execution Failed")
