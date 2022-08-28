xrandr --output Virtual-1 --mode 1920x1080

setxkbmap -layout us,ee,ru -option grp:alt_shift_toggle &

/usr/bin/pipewire &
/usr/bin/wireplumber &
/usr/bin/pipewire-pulse &
nm-applet &
blueman-applet &

picom &
feh --bg-fill /usr/share/WallPaper/KATI3.png &
