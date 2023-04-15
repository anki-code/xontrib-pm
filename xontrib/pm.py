"""Persistent aliases for package managers."""

from shutil import which as _which

_pm = {
    'apt': {    
        'install': 'sudo apt install',
        'instally': 'sudo apt install -y',
        'uninstall': 'sudo apt uninstall',
        'search': 'sudo apt search',
    },    
    'brew': {
        'install': 'brew install',
        'uninstall': 'brew uninstall',
        'search': 'brew search',
    },
    'pacman': { # Aliases from https://devhints.io/pacman
        'install': 'sudo pacman -Sy',
        'uninstall': 'sudo pacman -Rsc',
        'search': 'sudo pacman -Ss',
        'upgrade-everything': 'sudo pacman -Syu',
        'package-info': 'sudo pacman -Qii',
        'package-unneeded-list': 'sudo pacman -Qdt',
        'package-unneeded-uninstall': 'sudo pacman -Rns @($(pacman -Qdtq).splitlines())',
    },
    'port': {  # https://www.macports.org/
        'install': 'port install',
        'uninstall': 'port uninstall',
        'installed': 'port installed',
    },
    'yum': {    
        'install': 'sudo yum install',
        'instally': 'sudo yum install -y',
        'uninstall': 'sudo yum uninstall',
        'search': 'sudo yum search',
    },
    'zap': { # https://github.com/srevinsaju/zap
        'install': 'sudo zap install',
        'search': 'sudo zap search',
    },
    'guix': {
        'install': 'guix install',
        'uninstall': 'guix remove',
        'search': 'guix search',
        'upgrade-everything': 'guix upgrade',
        'package-info': 'guix show',
    },
}


_found_pm = []
for p in _pm.keys():
    if _which(p):
        _found_pm.append(p)
        aliases |= {p + '-' + alias : value for alias, value in _pm[p].items()} 

aliases['pm'] = f"echo {', '.join(_found_pm)}"
    
