# pycom2exe
Простая консольная утилита для преобразования пакета python в *.exe

```
usage: pycom2exe [-h] [-a APPNAME] [-d EXEDIR] [-v VERSION] [-e] [-i ICON] [-l {TRACE,DEBUG,INFO,WARN,ERROR,CRITICAL}] [-vf VERSION_FILE] [-c] [-w] script

positional arguments:
    script                Script that will be used for building executable file

optional arguments:
    -h, --help                                                                                       show this help message and exit
    -a APPNAME, --appname APPNAME                                                                    Name of executable file (default: name of script)
    -d EXEDIR, --exedir EXEDIR                                                                       Path where executable file will be created (default: ./exe)
    -v VERSION, --version VERSION                                                                    Version of executable file. If version is specified it will be added to the name of executable file (default: None)
    -e, --exclude-modules                                                                            Indicates that some modules must be excluded from bundle
    -i ICON, --icon ICON                                                                             Path to icon of executable file (default: None)
    -l {TRACE,DEBUG,INFO,WARN,ERROR,CRITICAL}, --log-level {TRACE,DEBUG,INFO,WARN,ERROR,CRITICAL}    Amount of detail in build-time console messages. LEVEL may be one of TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL (default: CRITICAL)
    -vf VERSION_FILE, --version-file VERSION_FILE                                                    Version file.
    -c, --console                                                                                    Open a console window for standard i/o (default)
    -w, --windowed                                                                                   Windows and Mac OS X: do not provide a console window for standard i/o. On Mac OS X this also triggers building an OS X .app bundle. This option is ignored in *NIX systems.
```