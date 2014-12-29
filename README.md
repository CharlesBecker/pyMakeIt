pyMakeIt
========

Python script to create barebones C++ and C++ header files.  

Not yet set up to take arguments from the command line.
Still just a work in progress.

Commandline arguments:
-h or --help prints help (not yet implemented)
-v prints version
--Verbose (requires capital V) turns on verbose mode (not yet implemented)
-m [filename] creates the file.  If the file does not end in .h it is created a a C++/.cpp file, if it nds in .h it is created as a C++ header file.
-n [name] gives the 'project' name.  This will be the directory where the files will be created.  If this is not given than the first part of the filename (before the .) is used instead.
-o override: if the project already exists then it will create the files in the directory.  If this is not set and the directory exists then the program exits without creating the files as a safety measure.  NOTE: if you turn this on it currently WILL overwrite files with the same names in the project directory (needs to be fixed for later versions?)

You will need to chang the #! in the makeIt.py file to point to the correct location on your system.

You will need to make the makeIt.py file executable.

Comments in Helper.py are not up to date.

Needs to be fully commented, refactored, have exception handling, pythonized, and more fully tested.

All text above is in relation to version 1.0 beta (2014-12-29)
