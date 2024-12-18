FILEPATH = 'text_files/todos.txt'

def get_todos(filepath=FILEPATH):
	""" Read a text files and return to the
	to-do list.
	"""
	with open(filepath, 'r') as file_local:
		# keep the data into list in "todos" variable
		todos_local = file_local.readlines()
	return todos_local


def write_todos(todos_ar, filepath=FILEPATH):
	""" Write a to-do list in to the text files."""
	with open(filepath, 'w') as file_local:
		file_local.writelines(todos_ar)