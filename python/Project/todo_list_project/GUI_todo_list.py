import functions
import FreeSimpleGUI as sg
import time

sg.theme('black')
clock = sg.Text('', key='clock')
label = sg.Text('Type your todo list')
input_text = sg.InputText(tooltip='enter todo', key='inputtext')
add_button = sg.Button(size=2, key='Add', tooltip='add todo', image_source='add.png')
list_box = sg.Listbox(values=functions.get_todos(), key='listbox',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button(size=2, key='Complete', tooltip='complete todo', image_source='complete.png')
exit_button = sg.Exit('Exit')

window = sg.Window('Todo list App',
                   layout=[[clock],
                           [label], [input_text, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Times New Roman', 15))

while True:
	events, values = window.read(timeout=20)
	window['clock'].update(value=time.strftime("%b %d, %Y %H:%M %S"))
	match events:
		case 'Add':
			todos = functions.get_todos()
			new_todos = values['inputtext'] + '\n'
			todos.append(new_todos)
			functions.write_todos(todos)
			window['listbox'].update(values=todos)
		case 'Edit':
			try:
				todo_to_edit = values['listbox'][0]
				new_todo = values['inputtext']

				todos = functions.get_todos()
				index = todos.index(todo_to_edit)

				todos[index] = new_todo
				functions.write_todos(todos)

				window['listbox'].update(values=todos)
			except IndexError:
				sg.popup('Please select an item', font=('times new roman', 15,))
		case 'listbox':
			window['inputtext'].update(value=values['listbox'][0])
		case 'Complete':
			try:
				todos = functions.get_todos()
				todo_to_complete = values['listbox'][0]
				todos.remove(todo_to_complete)
				functions.write_todos(todos)
				print(todos)
				window['listbox'].update(values=todos)
				window['inputtext'].update(value='')
			except IndexError:
				sg.popup('Please select an item', font=('times new roman', 15,))
		case 'Exit':
			break
		case sg.WIN_CLOSED:
			break

window.close()
