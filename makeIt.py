import Helper

file_name = "secondThing"
ext = "cpp"

helper = Helper.Helper(file_name, ext)

helper.getPrecompile()
helper.makeProject()
helper.writeFile()
