#!/bin/sh

read -r -p "A user sudo password need to be enter:" password

#Check what Linux distribution I am using
Distro=$(cat /etc/*-release | grep "^ID=")
Distro=$(echo "$Distro" | sed -r 's/[ID=]+//g')

# To install all needed dependencies and program
for ((i = 0 ; i <= 1; i++)); do
	case $Distro in
		arch)
			# --needed: Do not reinstall the targets that are already up-to-date. skips packages that up to date 
			# --noconfirm: Bypass any and all “Are you sure?” messages. auto yes
			# --refresh: Download a fresh copy of the master package.
			xargs sudo -S <<< $password pacman -S --refresh --needed --noconfirm < packageArch
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
			#Check what Linux distribution I am using is based on
			echo "$Distro was based on"
			Distro=$(cat /etc/*-release | grep "^ID_LIKE=")
			Distro=$(echo "$Distro" | sed -r 's/[ID_LIKE=]+//g')
			;;
	esac
done

# Downloading and Installing Metcha theme 
git clone https://github.com/vinceliuice/Matcha-gtk-theme.git
sudo -S <<< $password Matcha-gtk-theme/install.sh

# Downloading and Installing xkblayout
# Why? Needed to show your keyboard layout
git clone https://github.com/nonpop/xkblayout-state.git
make -C xkblayout-state/
sudo -S <<< $password cp -r xkblayout-state/xkblayout-state /bin/

# Downloading and Installing NerdFonts 
# Needed for the Glyths/Images
git clone https://github.com/ryanoasis/nerd-fonts.git
sudo -S <<< $password nerd-fonts/install.sh
sudo -S <<< $password mv /root/.local/share/fonts/NerdFonts /usr/share/fonts

# Downloading and Installing wallpaper
git clone https://github.com/alexkaasik/WallPaper.git
rm -rf WallPaper/.git
sudo -S <<< $password cp -r WallPaper /usr/share/

# Downloading modulo to check updates and to update the system
git clone https://github.com/alexkaasik/Update_Checker.git
sudo -S <<< $password cp -r Update_Checker /usr/share/

# why use .[^.]* not .* because could brick your user
cp -r ~/KAT-Qtile/.[^.]* ~/

sudo -S <<< $password reboot
