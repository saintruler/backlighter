# Backlighter
Server that helps change hardware screen brightness where xbacklight is not working.

# Install
Place `backlighter_server.py` to `/usr/local/bin/` and `backlighter.service` to `/etc/systemd/system/`.

Then enable and start service:

`sudo systemctl enable backlighter.service`

`sudo systemctl start backlighter.service`

# Usage
Place `backlighter.py` wherever you want. 

By default minimal brightness that can be set is 10%, by typing `python3 backlighter.py set_min %percent%`.

To actually change brightness type `python3 backlighter.py change %delta_percent%`. `delta_percent` can be negative.

If you want to set brightness to specific value type `python3 backlighter.py set %percent%`.

# backlighter_notify.sh
To create notifications when brightness changed use `backlighter_notify.sh`. Change path to `backlighter.py` and 
backlight directory path if necessary.

*`libnotify` should be installed on your system for this to work.*
