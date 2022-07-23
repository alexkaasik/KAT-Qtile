xrandr --output Virtual-1 --mode 1920x1080

setxkbmap -layout us,ee,ru -option grp:alt_shift_toggle &

/usr/bin/pipewire &
/usr/bin/wireplumber &
/usr/bin/pipewire-pulse &

picom &
feh --bg-fill /home/alex/images/WallPaper/KATI3.png &
exec qtile start
