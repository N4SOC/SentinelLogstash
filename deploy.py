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
    "table":None
}
for collector in config.collectors:
    if "table" in collector:
        args["table"]=collector["table"]
    else:
        args["table"]=None
    if os.path.isdir(f"./{collector['name']}"):
        if collector['proto'] == "tcp":
            ports = [f"{collector['port']}:514"]
        else:
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

buildcmd=subprocess.run(["docker", "compose", "build"])
if buildcmd.returncode==0:
    print(f"Build Successful - {len(services)} collectors built")
else:
    print("Build Failed")

runcmd=subprocess.run(["docker", "compose", "up", "-d"])
if runcmd.returncode==0:
    print(f"Execution Successful - {len(services)} collectors running")
else:
    print("Execution Failed")