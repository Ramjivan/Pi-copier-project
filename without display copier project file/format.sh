#!/bin/bash

#getting all mount points and storing to mpoints.txt
df -B1 | grep -vE '^Filesystem|tmpfs|cdrom' | awk '{ print $1 }'|tail -n +3 > mpoints.txt

#now getting all drives in an array usb

a=0
mountpoints="/home/pi/mpoints.txt"
  while IFS= read -r d
    do  
	#umount the drive
	umount "$d"
	sudo mkfs.vfat "$d" -n SANTVANI
	sudo -u pi udisksctl mount --block-device "$d"
    done <"$mountpoints"





sleep 1s
