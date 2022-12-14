if grep -i ubuntu /etc/os-release>/dev/null; then
    echo "Ubuntu Detected.. Installing"
    apt remove -y docker docker-engine docker.io containerd runc
    apt install -y apt-transport-https ca-certificates curl gnupg
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt update
    apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

elif grep -i debian /etc/os-release>/dev/null; then
    echo "Debian Detected.. Installing"
    apt remove -y docker docker-engine docker.io containerd runc
    apt install -y apt-transport-https ca-certificates curl gnupg
    curl -fsSL https://download.docker.com/linux/debian/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
    echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null
    apt update
    apt install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin

elif grep -i photon /etc/os-release>/dev/null; then
    echo "Docker already installed by default in PhotonOS - Skipping to Docker Compose"
    tdnf install docker-compose-plugin

elif grep -i CentOS /etc/os-release>/dev/null; then
    echo "CentOS Detected.. Installing"
    yum remove -y docker docker-engine docker.io containerd runc
    yum install -y yum-utils
    yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
    yum update
    yum install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    systemctl start docker

else
    echo "Automatic instllation on this OS not supported"
fi
