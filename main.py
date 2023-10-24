import os
from file_parse import process_files, write_file

current_directory = os.getcwd()
directory_path = os.path.join(current_directory, 'files')

result = process_files(directory_path)

write_file('output.txt', result)
