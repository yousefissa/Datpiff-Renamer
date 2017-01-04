# datpiff renamer
# author - github.com/yousefissa

import os

user_path = input('Copy the directory where you want to change file names.\n>>> ')
print('The entered directory is: {}'.format(user_path))


continue_prompt = input('Would you like to continue? Enter only "yes" if you would.\n>>> ')
if continue_prompt.lower() != 'yes':
	quit()

replacing_phrase = '(DatPiff Exclusive)'


for filename in os.listdir(user_path):
	if replacing_phrase in filename:
		new_file_name = filename.replace(replacing_phrase, '')
		old_path = os.path.join(user_path, filename)
		new_path = os.path.join(user_path, new_file_name)
		os.rename(old_path, new_path)

	else:
		print('{} did not have the (DatPiff Exclusive) in it'.format(filename))

print('Done renaming. ')
print('The folder contents are now:\n{}'.format(os.listdir(user_path)))


