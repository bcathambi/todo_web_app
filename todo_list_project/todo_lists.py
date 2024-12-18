import functions
import time



now = time.strftime("%b %d, %H:%M:%S")
print("It is", now)
while True:
	# Get user input and remove the spaces using strip()
	user_input = input("Enter add, show, edit, complete or exit: ")
	user_input = user_input.strip()

	if user_input.startswith('add'):
		todo = user_input[4:] + "\n"
		todo = todo.title()

		todos = functions.get_todos()

		todos.append(todo)

		functions.write_todos(todos)

	elif user_input.startswith('show'):

		todos = functions.get_todos()

		# new_todo = [item.strip('\n') for item in todos]

		for index, item in enumerate(todos):
			item = item.strip('\n')
			row = f"{index + 1}-{item}"
			print(row)

	elif user_input.startswith('edit'):
		try:
			numbers = int(user_input[5:])
			numbers = numbers - 1

			todos = functions.get_todos()

			new_todo = input("Enter new item: ")
			todos[numbers] = new_todo.title() + '\n'

			functions.write_todos(todos)

		except ValueError:
			print("Please enter values")
			continue

	elif user_input.startswith('complete'):
		try:
			numbers = int(user_input[9:])
			numbers = numbers - 1

			todos = functions.get_todos()

			remove_todos = todos[numbers].strip('\n')
			removed_todos = f'{numbers + 1}-{remove_todos}'

			# pop function would eliminate the lists
			todos.pop(numbers)

			functions.write_todos(todos)

			print(f"Todo '{removed_todos}' was removed from the lists")
		except IndexError:
			print("Your command is not valid")
			continue

	elif user_input.startswith('exit'):
		break

	else:
		print(f"Invalid inputs typed - {user_input}, please try again")
