import os

path_folder = r'\\'

print()
print('Path: {}'.format(path_folder))
print()
old_extension = '.' + input('Old extension: ')
new_extension = '.' + input('New extension: ')
print()

files_counter = 0

with os.scandir(path_folder) as files_and_folders:
	for element in files_and_folders:
		if element.is_file():
			tuple_root_ext = os.path.splitext(element.path)
			root = tuple_root_ext[0]  # filename
			ext = tuple_root_ext[1]  # file extension

			if ext == old_extension:
				new_path = root + new_extension
				os.rename(element.path, new_path)
				files_counter += 1

print()
print('Changing from {} to {}'.format(old_extension, new_extension))
print('Files changed: {}'.format(files_counter))
