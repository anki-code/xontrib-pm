"""Persistent aliases for package managers."""

import shutil as _shutil

if 'pm' in aliases:
    print("xontrib-pm: 'pm' is already in aliases, skip loading")    

elif _shutil.which('pacman'):
    # Aliases from https://devhints.io/pacman
    aliases |= {
        'pm': 'echo pacman',
        'pm-install': 'sudo pacman -Sy',
        'pm-uninstall': 'sudo pacman -Rsc',
        'pm-search': 'sudo pacman -Ss',
        'pm-upgrade-everything': 'sudo pacman -Syu',
        'pm-package-info': 'sudo pacman -Qii',
        'pm-package-unneeded-list': 'sudo pacman -Qdt',
        'pm-package-unneeded-uninstall': 'sudo pacman -Rns @($(pacman -Qdtq).splitlines())',
    }
    
elif _shutil.which('apt'):
    aliases |= {    
        'pm': 'echo apt',
        'pm-install': 'sudo apt install',
        'pm-instally': 'sudo apt install -y',
        'pm-uninstall': 'sudo apt uninstall',
        'pm-search': 'sudo apt search',
    }

elif _shutil.which('yum'):
    aliases |= {    
        'pm': 'echo yum',
        'pm-install': 'sudo yum install',
        'pm-instally': 'sudo yum install -y',
        'pm-uninstall': 'sudo yum uninstall',
        'pm-search': 'sudo yum search',
    }    

elif _shutil.which('zap'):  # https://github.com/srevinsaju/zap
    aliases |= {    
        'pm': 'echo zap',
        'pm-install': 'sudo zap install',
        'pm-search': 'sudo zap search',
    }    
