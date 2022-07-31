#!/bin/sh

#echo "A user sudo password need to be enter:" 

read -r -p "A user sudo password need to be enter:" password

Distro=$(cat /etc/*-release | grep "^ID=")
Distro=$(echo "$Distro" | sed -r 's/[ID=]+//g')

for ((i = 0 ; i <= 1; i++)); do
	case $Distro in
		arch)
			xargs sudo -S <<< $password pacman -Sy --needed --noconfirm < packageArch
			break
			;;
		fedora)
			xargs sudo -S <<< $password dnf -y install < packageFedora
			break
			;;
		debian)
			xargs sudo -S <<< $password apt-get -y install < packageDeb
			break
			;;
		ubuntu)
			xargs sudo -S <<< $password apt-get -y install < packageDeb
			break
			;;
		*)
			echo "$Distro was based on"
			Distro=$(cat /etc/*-release | grep "^ID_LIKE=")
			Distro=$(echo "$Distro" | sed -r 's/[ID_LIKE=]+//g')
			;;
	esac
done

git clone https://github.com/vinceliuice/Matcha-gtk-theme.git
git clone https://github.com/ryanoasis/nerd-fonts.git
git clone https://github.com/nonpop/xkblayout-state.git

sudo -S <<< $password Matcha-gtk-theme/install.sh
make -C xkblayout-state/
sudo -S <<< $password cp xkblayout-state/xkblayout-state /bin/
sudo -S <<< $password nerd-fonts/install.sh

rm -rf .git
mv ~/KAT-Qtile/.[^.]* ~/

rm -rf KAT-Qtile && sudo -S <<< $password reboot
