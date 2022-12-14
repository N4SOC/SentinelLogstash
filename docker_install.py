import subprocess


def checkDocker():
    if runcmd("docker ps") == 0:
        print("Docker is already Installed")
    else:
        print("Docker not Installed")

def installDocker():
    exitcode=0
    try:
        print("Cleaning up old docker packages")
        exitcode+=runcmd("apt remove -y docker docker-engine docker.io containerd runc")
        print("Adding Prerequisites")
        exitcode+=runcmd("apt install -y apt-transport-https ca-certificates curl gnupg")
        print("Adding Apt Repo Key")
        exitcode+=runcmd("curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg")
        print("Adding Apt Repo")
        exitcode+=runcmd('echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list')
        print("Updating Apt")
        exitcode+=runcmd("apt update")
        print("Installing Docker Packages")
        exitcode+=runcmd("apt install -y docker-ce docker-ce-cli containerd.io")
        print("Installing Docker Compose Plugin")
        exitcode+=runcmd("apt install -y docker-compose-plugin")
    except:
        print("Something failed - please review output")
    if exitcode == 0:
        print("Installation Sucesful")
    else:
        print("Something failed - please review output")