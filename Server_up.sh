# This is a server-up script

# chmod +x Server_up.sh
# ./Server_up.sh

sudo apt update
sudo apt full-upgrade

sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io

sudo systemctl start docker
sudo systemctl enable docker
sudo systemctl status docker

sudo curl -L "https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

sudo apt autoremove

# mount sdb volume
sudo mkdir -p /mnt/data
sudo mkfs.ext4 /dev/sdb
sudo mount /dev/sdb /mnt/data
sudo chmod 777 /mnt/data

# Get the code:
git clone https://github.com/kertser/Authenticator
# shellcheck disable=SC2164
cd Authenticator
docker-compose up -d