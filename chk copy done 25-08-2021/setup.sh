#!/bin/bash

#give pi user sudo root priveleges 
sudo usermod -aG  sudo pi

#making bash files executable
chmod +x copy.sh
chmod +x cpo.sh
chmod +x copier.py
chmod +x /etc/rc.local

sudo echo 'done' > ~/copy_completed.txt

# startup script | adding to rc.local
sudo echo '#!/bin/sh -e

python3 /home/pi/copier.py &

exit 0' > /etc/rc.local



