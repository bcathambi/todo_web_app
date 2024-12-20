import functions
import FreeSimpleGUI as sg

label = sg.Text('Type your todo list')
input_text = sg.InputText(tooltip='enter todo', key='inputtext')
add_button = sg.Button('Add')
list_box = sg.Listbox(values=functions.get_todos(), key='listbox',
                      enable_events=True, size=[45, 10])
edit_button = sg.Button('Edit')
complete_button = sg.Button('Complete')
exit_button = sg.Exit('Exit')

window = sg.Window('Todo list App',
                   layout=[[label], [input_text, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Times New Roman', 15))

while True:
	events, values = window.read()
	print(events)
	print(values)
	print(values['listbox'])
	match events:
		case 'Add':
			todos = functions.get_todos()
			new_todos = values['inputtext'] + '\n'
			todos.append(new_todos)
			functions.write_todos(todos)
			window['listbox'].update(values=todos)
		case 'Edit':
			todo_to_edit = values['listbox'][0]
			new_todo = values['inputtext']

			todos = functions.get_todos()
			index = todos.index(todo_to_edit)

			todos[index] = new_todo
			functions.write_todos(todos)

			window['listbox'].update(values=todos)
			print('listbox:',len(values['listbox']))
		case 'listbox':
			window['inputtext'].update(value=values['listbox'][0])
		case 'Complete':
			todos = functions.get_todos()
			todo_to_complete = values['listbox'][0]
			todos.remove(todo_to_complete)
			window['listbox'].update(values=todos)
			window['inputtext'].update(value='')
		case 'Exit':
			exit()
		case sg.WIN_CLOSED:
			break
window.close()
