"""Persistent aliases for package managers."""

import shutil as _shutil

if 'pm' in aliases:
    print("xontrib-pm: 'pm' is already in aliases, skip loading")    

elif _shutil.which('pacman'):
    # Aliases from https://devhints.io/pacman
    aliases['pm'] = 'echo pacman'
    aliases['pm-install'] = 'sudo pacman -Sy'
    aliases['pm-uninstall'] = 'sudo pacman -Rsc'
    aliases['pm-search'] = 'sudo pacman -Ss'
    aliases['pm-upgrade-everything'] = 'sudo pacman -Syu'
    aliases['pm-package-info'] = 'sudo pacman -Qii'
    aliases['pm-package-unneeded-list'] = 'sudo pacman -Qdt'
    aliases['pm-package-unneeded-uninstall'] = 'sudo pacman -Rns @($(pacman -Qdtq).splitlines())'

elif _shutil.which('apt'):
    aliases['pm'] = 'echo apt'
    aliases['pm-install'] = 'sudo apt install'
    aliases['pm-uninstall'] = 'sudo apt uninstall'
    aliases['pm-search'] = 'sudo apt search'
