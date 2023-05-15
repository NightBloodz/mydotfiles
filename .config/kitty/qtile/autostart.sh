#!/bin/sh
feh --bg-scale ~/images/hollow.jpg
picom -b -c --corner-radius 15 --active-opacity 95 --shadow-radius 12
~/.screenlayout/screen.sh
alttab -sc 0 -d 0 -w 1 & disown
