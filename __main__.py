#!/usr/bin/env python

"""
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
"""

# import packages and modules
import argparse
import json
import os
import os.path
import sys

def rename(oldname, newname):
	"""
		Rename file.
		
		:param str oldname:
		    Old name of file.
			
		:param str newname:
		    New name of file.
			
		:return None:
	"""
	if oldname != newname and os.path.exists(oldname):
		if os.path.exists(newname):
			os.remove(newname)
		os.rename(oldname, newname)

if __name__ == "__main__":
	# show help if command will be runned 
	# without arguments
	if not len(sys.argv[1:]):
		sys.argv.append("-h")

	# create cmd parser
	parser = argparse.ArgumentParser(prog = "pycom2exe", prefix_chars = "-")
	# add cmd args
	parser.add_argument("script", type = str, help = "Script that will be used for building executable file")
	parser.add_argument("-a", "--appname", default = None, type = str, help = "Name of executable file (default: name of script)")
	parser.add_argument("-d", "--exedir", default = os.path.join(os.path.dirname(__file__), "exe"), type = str, help = "Path where executable file will be created (default: ./exe)")
	parser.add_argument("-v", "--version", default = None, type = str, help = "Version of executable file. If version is specified it will be added to the name of executable file (default: None)")
	parser.add_argument("-e", "--exclude-modules", action = "store_true", help = "Indicates that some modules must be excluded from bundle")
	parser.add_argument("-i", "--icon", default = None, type = str, help = "Path to icon of executable file (default: None)")
	parser.add_argument("-l", "--log-level", choices = ["TRACE", "DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"], default = "CRITICAL", type = str, help = "Amount of detail in build-time console messages. LEVEL may be one of TRACE, DEBUG, INFO, WARN, ERROR, CRITICAL (default: CRITICAL)")
	parser.add_argument("-vf", "--version-file", default = None, type = str, help = "Version file.")
	parser.add_argument("-c", "--console", action = "store_true", help = "Open a console window for standard i/o (default)")
	parser.add_argument("-w", "--windowed", action = "store_true", help = "Windows and Mac OS X: do not provide a console window for standard i/o. On Mac OS X this also triggers building an OS X .app bundle. This option is ignored in *NIX systems.")
	# parse cmd args
	args = parser.parse_args()
	
	if os.path.exists(os.path.abspath(args.script)):
		script = args.script
	else:
		print("Script does not exists - %s" % os.path.abspath(args.script))
		sys.exit()
	
	# get application name
	appname = args.appname if args.appname else os.path.splitext(os.path.basename(script))[0]
	
	# set distribution directories
	distpath = os.path.join(args.exedir, "dist")
	buildpath = os.path.join(args.exedir, "build")
	specpath = args.exedir
	
	# set log level
	loglevel = args.log_level.upper()
	
	# get list of modules that 
	# must be excluded from bundle
	excludes = []
	if args.exclude_modules:
		with open(os.path.join(os.path.dirname(__file__), "exclude-modules.json"), "r") as f:
			try: excludes = json.loads(f.read())[appname]
			except KeyError:
				print('Can not find any excluded modules for "%s"' % appname)
				sys.exit()
			except Exception as ex:
				print("Can not read configurate file. Reason: %s" % str(ex))
				sys.exit()
	
	# add version to application name
	if args.version:
		appname += "-" + args.version
	
	# create command
	command = 'py -%d.%d -m PyInstaller "%s" --log-level "%s" --clean -F --distpath "%s" --workpath "%s" --specpath "%s"' % ( sys.version_info[:2] + (script, loglevel, distpath, buildpath, specpath,) )
	if args.icon != None:
		command += ' -i "%s"' % args.icon
	command += ' --win-private-assemblies --win-no-prefer-redirects'
	for module in excludes:
		command += " --exclude-module %s" % module
	# add version file arg to command
	if args.version_file != None:
		if os.path.exists(args.version_file) and os.path.isfile(args.version_file):
			command += ' --version-file "%s"' % args.version_file
	# add binary option
	if args.console and args.windowed:
		print("Build file may be only consoled or windowed")
		sys.exit()
	elif args.console:
		command += " -c"
	elif args.windowed:
		command += " -w"
		
	print(">>> " + command)
	# execute command
	os.system(command)
	# rename executable file
	rename(os.path.join(distpath, "%s.exe" % os.path.basename(script).split(".")[0]), os.path.join(distpath, "%s.exe" % appname))
