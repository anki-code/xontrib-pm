<p align="center">
Persistent aliases for package managers.
</p>

<p align="center">  
If you like the idea click ⭐ on the repo and <a href="https://twitter.com/intent/tweet?text=Nice%20xontrib%20for%20the%20xonsh%20shell!&url=https://github.com/anki-code/xontrib-jump-to-dir" target="_blank">tweet</a>.
</p>

## Installation

To install use pip:

```bash
xpip install xontrib-pm
# OR: xpip install -U git+https://github.com/anki-code/xontrib-pm
```

## Usage

After loading xontrib-pm is searching the known package managers. If the package manager installed (e.g. `pacman`) the xontrib adds the aliases e.g. `pacman-install`, `pacman-search`, etc. The `pm` command returns the list of known installed package managers.

```xsh
xontrib load pm
pm
# pacman, brew

# Type `pacman-` and press Tab
pacman-search vim    # sudo pacman -Ss vim
pacman-install vim   # sudo pacman -Sy vim
```

Feel free to extand the list of known package managers.

## Supported package managers

PMs: `apt`, `brew`, `guix`, `pacman`, `port`, `yum`, `zap`. Feel free to add more, PR is welcome!

## Commands

The list of commands that need to have the package manager aliases i.e. `<package_manager>-<command>`:
* `search` - serach the package
* `install` - install the package
* `uninstall` - uninstall the package

Optinally:
* `instally` (install and say yes) - install without user confirmation
* `installed` - list of installed packages
* Any other useful aliases e.g. `pacman-upgrade-everything`.

## Credits

* [Package manager-independent bash aliases](https://gist.github.com/rroblak/8137276)
* This package was created with [xontrib template](https://github.com/xonsh/xontrib-template).
