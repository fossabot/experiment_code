sudo apt-get install ibus-rime
sudo apt-get install docker.io
sudo apt-get install docker-compose
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt-get -f install libappindicator1 libindicator7
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo usermod -aG docker bb8
sudo apt-get install htop
sudo apt-get install python-pip python-dev build-essential
curl "https://raw.githubusercontent.com/niasand/cool-config/master/vimrc.sh" -o "vimrc.sh"
chmod +x vimrc.sh
./vimrc.sh
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
sudo apt-get install tree
curl -sSL https://get.docker.com/ubuntu/ | sudo sh

sudo rm /var/crash/*
