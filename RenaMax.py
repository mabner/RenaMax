import os

path_folder = r'.'

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

		# Using multiple assignments
            # filename, extension
            root, ext = os.path.splitext(element.path)

            if ext == old_extension:
                new_path = root + new_extension
                os.rename(element.path, new_path)
                files_counter += 1
                print(format(new_path))

print()
print('Changing from {} to {}'.format(old_extension, new_extension))
print('Files changed: {}'.format(files_counter))
