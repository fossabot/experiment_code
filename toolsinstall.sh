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
cd ~/Documents/ && git clone https://github.com/niasand/cool-config.git
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
python get-pip.py
sudo apt-get install tree
sudo pip install -r ~/Documents/cool-config/requirements.txt
sudo wget -qO- https://get.docker.com/ | sh
wget https://storage.googleapis.com/golang/go1.5.3.linux-amd64.tar.gz
sudo apt-get install bison ed gawk gcc libc6-dev make
sudo rm /var/crash/*
