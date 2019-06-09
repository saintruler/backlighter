#!/bin/sh

$HOME/.scripts/system/backlighter.py "$@"


backlight_path="/sys/class/backlight/amdgpu_bl0"
max_brightness=$(cat "$backlight_path/max_brightness")
current_brightness=$(cat "$backlight_path/brightness")

percent=$(python -c "print(int(float($current_brightness)/float($max_brightness)*100))")

notify-send -t 1000 "Brightness set to $percent%"
