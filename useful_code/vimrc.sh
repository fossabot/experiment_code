#!/usr/bin/env bash
sudo apt-get install -y git
sudo apt-get install -y vim
sudo apt-get install -y ctags
mkdir ~/.vim
mkdir ~/.vim/bundle
git clone https://github.com/gmarik/vundle.git ~/.vim/bundle/vundle
git clone https://github.com/fyffyt/vim-configuration.git ~/.vim/dot-vimrc
cp ~/.vim/dot-vimrc/bundles.vim ~/.vim/
cp ~/.vim/dot-vimrc/vimrc ~/.vimrc
cp -r ~/.vim/dot-vimrc/bundle/* ~/.vim/bundle/
