#!/usr/local/bin/python3
import getopt
import sys
import Helper

def print_help():
	print("This will be the help info")

def makeit(value):
	results = dict()
	results['filename'], results['ext'] = value.split(".")
	return results

def create(value):
	if (value['project'] is None):
		value['project'] = value['filename']
	project_name = value['project']
	file_name = {'filename': value['filename'], 'ext': value['ext']}
	override = value['override']
	helper = Helper.Helper(project_name, file_name, override)

	helper.getPrecompile()
	helper.makeProject()
	helper.writeFile()

def main(value, control):
	do_it = False
	print("Here")
	for opt, arg in options:
		if opt in ('-o'):
			control['override'] = True
			print("Override is: " + str(control['override']))
		elif opt in ('--Verbose'):
			control['verbose'] = True
			print("Verbose mode is not yet implemented")
		elif opt in ('-v'):
			print("Version " + str(control['version']) + " of makeIt by Charles Becker")
		elif opt in ('-h', '--help'):
			print_help()
		elif opt in ('-m'):
			w = dict()
			w = makeit(arg)
			control['filename'] = w['filename']
			control['ext'] = w['ext']
			print(arg)
			do_it = True
		elif opt in ('-n'):
			control['project'] = arg
	if(do_it == True):
		create(control)
	else:
		print("No file/project name was provided.")


options, remainder = getopt.getopt(sys.argv[1:], 'hm:vn:o', ['Verbose',
                                                              'help'
                                                              ])

control_array = dict()
control_array['override'] = False
control_array['verbose'] = False
control_array['version'] = '1.0'
control_array['project'] = None


if (__name__ == "__main__"):
	main(sys.argv[1:], control_array)
