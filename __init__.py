#!/usr/bin/env python

"""
	usage: pycom2exe [-h] [-a APPNAME] [-d EXEDIR] [-v VERSION] [-e] [-i ICON][-l LOG_LEVEL] script
	
	positional arguments:
	    script 									Script that will be used for building executable file

	optional arguments:
	    -h, --help 								show this help message and exit
	    -a APPNAME, --appname APPNAME 			Name of executable file (default: name of script)
	    -d EXEDIR, --exedir EXEDIR 				Path where executable file will be created (default: ./exe)
	    -v VERSION, --version VERSION 			Version of executable file. If version is specified it will be added to the name of executable file (default: None)
	    -e, --exclude-modules 					Indicates that some modules must be excluded from bundle
	    -i ICON, --icon ICON 					Path to icon of executable file (default: None)
	    -l LOG_LEVEL, --log-level LOG_LEVEL 	Amount of detail in build-time console messages. LEVEL may be one of TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL (default: CRITICAL)
"""

# Define metadata
__version__     = "1.0.0"
__author__      = "Vladimir Saltykov"
__copyright__   = "Copyright 2018, Vladimir Saltykov"
__email__       = "vowatchka@mail.ru"
__license__     = "MIT"
__date__        = "2018-08-16"
