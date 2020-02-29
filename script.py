# libraries
import os
import sys

# function to make full paths
def make_full_path(parent_dir, files):
	full_paths = []
	for i in range(len(files)):
		full_paths.append(os.path.join(parent_dir, files[i]))
	return full_paths

# function to search for search_string in a given file
def search_for_searchstring(file_path, search_string):
	file_ptr = file(file_path, "r")
	lines = file_ptr.readlines()
	for i in range(len(lines)):
		if(lines[i].find(search_string) != -1):
			print(i + 1, file_path)

# get directory path and if it doesn't exists, then terminate execution
search_dir = raw_input("Enter the path of Directory: ")
if(os.path.exists(search_dir) == False):
	print("x x x Path Not Found x x x")
	sys.exit(0)

# check if the entered path is directory or not, if not, then terminate execution
if(os.path.isdir(search_dir) == False):
	print("x x x Entered path is not a directory x x x")
	sys.exit(0)

# get type of file look into for search string
file_types = raw_input("Enter comma-separated file extensions (NO SPACE, WITHOUT DOT) to look for search string: ")
# check extension list should not have space, if space is there, terminate execution
if(file_types.find(" ") != -1):
	print("x x x Found spaces x x x")
	sys.exit(0)
file_types = file_types.split(",")

# get search string
search_string = raw_input("Enter search string: ")

# search in all files under each sub-directory
files = os.listdir(search_dir)
paths_list = make_full_path(search_dir, files)
i = 0
while(i < len(paths_list)):
	current_path = paths_list[i]
	# if current_path is a directory
	if(os.path.isdir(current_path) == True):
		files = os.listdir(current_path)
		paths_list = paths_list + make_full_path(current_path, files)
	# if current_path is a file
	if(os.path.isfile(current_path) == True):
		filename = current_path.split("/")[len(current_path.split("/")) - 1]
		if(len(filename.split(".")) > 1):
			file_extension = current_path.split(".")[1]
			if((file_extension in file_types) == True):
				search_for_searchstring(current_path, search_string)
	# increment index var
	i = i + 1
