"""Persistent aliases for package managers."""

import shutil as _shutil

_pm = {
    'brew': {
        'pm': 'echo brew',
        'pm-install': 'brew install',
        'pm-uninstall': 'brew uninstall',
        'pm-search': 'brew search',
    },
    'pacman': { # Aliases from https://devhints.io/pacman
        'pm': 'echo pacman',
        'pm-install': 'sudo pacman -Sy',
        'pm-uninstall': 'sudo pacman -Rsc',
        'pm-search': 'sudo pacman -Ss',
        'pm-upgrade-everything': 'sudo pacman -Syu',
        'pm-package-info': 'sudo pacman -Qii',
        'pm-package-unneeded-list': 'sudo pacman -Qdt',
        'pm-package-unneeded-uninstall': 'sudo pacman -Rns @($(pacman -Qdtq).splitlines())',
    },
    'apt': {    
        'pm': 'echo apt',
        'pm-install': 'sudo apt install',
        'pm-instally': 'sudo apt install -y',
        'pm-uninstall': 'sudo apt uninstall',
        'pm-search': 'sudo apt search',
    },
    'yum': {    
        'pm': 'echo yum',
        'pm-install': 'sudo yum install',
        'pm-instally': 'sudo yum install -y',
        'pm-uninstall': 'sudo yum uninstall',
        'pm-search': 'sudo yum search',
    },
    'zap': { # https://github.com/srevinsaju/zap
        'pm': 'echo zap',
        'pm-install': 'sudo zap install',
        'pm-search': 'sudo zap search',
    }
}


def _get_default_pm():
    for pm in _pm.keys():
        if _shutil.which(pm):
            return pm
    return None

_XONTRIB_PM = __xonsh__.env.get('XONTRIB_PM', _get_default_pm())

if _XONTRIB_PM:
    aliases |= _pm[_XONTRIB_PM]
