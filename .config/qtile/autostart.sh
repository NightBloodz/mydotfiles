#!/bin/sh

picom -b -c --corner-radius 20 --legacy-backends 2>/dev/null

feh --bg-fill /home/alvaro/images/georgi-madzharov-cover-final-full-scene.jpg &

xfce4-power-manager
