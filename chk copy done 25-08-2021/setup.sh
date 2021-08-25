#!/bin/bash

#give pi user sudo root priveleges 
sudo usermod -aG  sudo pi

#making bash files executable
chmod +x copy.sh
chmod +x cpo.sh
#chmod +x copier.py

sudo echo 'python copier.py' >> .

sudo echo 'done' > ~/copy_completed.txt

