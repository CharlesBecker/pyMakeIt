#!/usr/local/bin/python3 
# change the #! to the proper version for your system
# also make the file executable

import getopt
import sys
import Helper

project_name = "firstThing"
file = "thirdThing"
ext = "cpp"
file_name = {'filename': file, 'ext': ext}


helper = Helper.Helper(project_name, file_name, True) 
# Note: this prototype defaults to true

helper.getPrecompile()
helper.makeProject()
helper.writeFile()
