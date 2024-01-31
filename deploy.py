#!/usr/bin/python3
import sys
import subprocess
import os
import config
from genericpath import isdir
from copy import deepcopy


def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


try:
    import yaml
except ImportError as e:
    install("pyyaml")
    import yaml

if os.geteuid() != 0:
    print("Script must be run as root, try using sudo...")
    sys.exit()

services = {}
args = {
    "environment_name": config.envName,
    "workspaceID": config.workspaceID,
    "workspaceKey": config.workspaceKey,
    "table": None
}


def runcmd(cmd):  # Wrapper to make running commands quicker
    runcmd = subprocess.run(cmd.split(" "))
    return runcmd.returncode


def installUpdater():
    cwd = os.getcwd()
    cronScript = f"""
    #!/usr/bin/env bash
    cd "{cwd}"
    /usr/bin/git pull
    /usr/local/bin/docker compose build
    /usr/local/bin/docker compose up -d --force-recreate
    """
    with open("/etc/cron.daily/sentinel_docker_refresh.sh", "w") as f:
        f.write(cronScript)
    runcmd("chmod +x /etc/cron.daily/sentinel_docker_refresh.sh")


for collector in config.collectors:
    args["table"] = None
    if "table" in collector:  # If custom table is defined for collector
        args["table"] = collector["table"]
    else:
        args["table"] = collector['name']
    if os.path.isdir(f"./{collector['name']}"):  # Confirm collector exists
        if collector['name'] == "ids":
            print("Automated IDS deplotyment not yet available")
        else:
            if collector['proto'] == "tcp":
                ports = [f"{collector['port']}:514"]
            else:  # If syslog is UDP
                ports = [f"{collector['port']}:514/udp"]
            service = {"build": {
                "context": f"./{collector['name']}",
                "args": deepcopy(args)
            },
                "image": f"{collector['name']}_sentinel",
                "restart": "always",
                "ports": ports
            }
            services[collector['name']] = service
    else:
        print(f"Collector not found: {collector['name']}, please check configuration")

yml = yaml.dump({"services": services})

with open("docker-compose.yml", "w") as f:
    f.write(yml)

if runcmd("docker compose down --remove-orphans") == 0:
    print(f"Stopped existing containers")
else:
    print("Stop Failed")

if runcmd("docker compose build") == 0:
    print(f"Build Successful - {len(services)} collectors built")
else:
    print("Build Failed")

if runcmd("docker compose up -d") == 0:
    print(f"Execution Successful - {len(services)} collectors running")
else:
    print("Execution Failed")

installUpdater()
