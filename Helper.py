#Helper module

import os

class Helper(object):

	def __init__(self, project_name, file_name, override = False):
		"""Set up everything for the project and file creation"""
		self.full_filename = file_name['filename'] + "." + file_name['ext']
		self.project = project_name
		self.project_path = os.getcwd() + "/" + self.project
		self.precompile = {}
		self.encoding = "utf-8"
		self.file_name = file_name
		self.file_ext = file_name['ext']
		self.override = override
		self.standard = "#include <iostream>\n\n"
		if (file_name['ext'] == "h"):
			self.is_header = True
		else:
			self.is_header = False
        

	def doesExist(self, target = None):
		"""	Checks to see if a file or directory exists
			Postcondition:
			Returns True if it does, False if it dosen't. """
	
		if (target == None):
			target = self.project
		
		if (os.path.exists(target)):
			return True
		else:
			return False
			
	def makeProject(self):
		"""	Creates the directory for the project
			Postcondition: 
			If the directory existed then the program quits.
			If the directory does not exist then it is created.
			If self.override is True then the directory is created regardless. """
			
		if(self.doesExist(self.project) == False):
			os.mkdir(self.project)
		elif((self.doesExist(self.project) == True) and (self.override == False)):
			quit("That project already exists.")
		elif((self.doesExist(self.project) == True) and (self.override == True)):
			# Project already exists, we'll just add it to the directory
			True
	
	def getPrecompile(self):
		"""	Creates the Precompiler definitions if this is a header file
			Postcondition:
			self.precompile dictionary is populated. """
		
		self.precompile["ifndef"] = "#ifndef H_{0}".format(self.file_name['filename'].upper())
		self.precompile["define"] = "#define H_{0}".format(self.file_name['filename'].upper())
		self.precompile["end"] = "#endif"
		
	def writeFile(self):
		"""	Writes the file
			Postcondition:
			Correct file is created. """
		os.chdir(self.project_path)
		if(self.doesExist((self.full_filename) == False) or (self.override == True)):
			fout = open(self.full_filename, "wb")
			if (self.is_header == True):
				self.writeHeader(fout)
			else:
				self.writeCPP(fout)
				
			if (self.is_header == True):
				self.writeFooter(fout)
			fout.close()
		else:
			quit("That file already exists.")


	def writeCPP(self, out_file):
		"""	Writes a standard barebones C++ file for you to use.
			Postcondition:
			C++ (cpp) file is created in the project directory. """
		
		out_file.write(bytes(self.standard, self.encoding))
		out_file.write(bytes("int main()\n", self.encoding))
		out_file.write(bytes("{\n\n", self.encoding))
		out_file.write(bytes("}", self.encoding))
					
	def writeHeader(self, out_file):
		""" If the file is a header file this outputs the precompiler opening directives.
			Postcondition:
			File has header file precompiler opening directives written to it. """
		out_file.write(bytes(self.precompile['ifndef'], self.encoding))
		out_file.write(bytes("\n", self.encoding))
		out_file.write(bytes(self.precompile['define'], self.encoding))
		out_file.write(bytes("\n", self.encoding))
		out_file.write(bytes(self.standard, self.encoding))
		
	def writeFooter(self, out_file):
		""" If the file is a header file this outputs the precompiler closing directives.
			Postcondition:
			File has header file precompiler closing directives written to it. """
		out_file.write(bytes(self.precompile['end'], self.encoding))


