#!/bin/sh
# Merge Resources
userresources=$HOME/.config/X11/Xresources
if [ -f "$userresources" ]; then
    xrdb -merge "$userresources"
fi

# Set Keyboard Layout
localectl set-keymap --no-convert us

# Detect Monitors & Ensure Order
xrandr --auto
xrandr --output HDMI-0 --right-of DP-0

# Add Background Image
feh --bg-scale ~/Pictures/wallpaper.jpg

# Start redshift
systemctl --user start redshift.service

# Launch Window Manager
i3
