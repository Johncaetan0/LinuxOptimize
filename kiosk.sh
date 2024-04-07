#!/bin/bash
xset s noblank
xset s off
xset
dpms
unclutter idle 0.5 -root &
/home/pi/.config/chromi
sed -i 's/"exited_cleanly": false/"exited_cleanly":true/'/home/pi/.config/chromium/Default/Preferences
sed -i 's/"exit_type": "Crashed"/"exit_type": "Normal"/ /home/pi/.config/chromium/Default/Preferences
/usr/bin/chromium-browser --autoplay-policy-no-user-gesture-required --noerrdialogs --disable-infobars --kiosk http://131.107.1.142:3051/index.html/7
5 &
while true; do
xdotool keydown ctrl+Tab; xdotool keyup ctrl+Tab;
sleep 20
done