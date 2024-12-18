import functions
import FreeSimpleGUI as sg

lable = sg.Text('Type your todo list')
input_text = sg.InputText()
add_button = sg.Button('Add')

window = sg.Window('Todo list App', layout=[[lable],[input_text,add_button]])
window.read()
window.close()