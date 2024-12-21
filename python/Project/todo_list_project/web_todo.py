import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
	todo = st.session_state['new_todo'] + '\n'
	todos.append(todo)
	functions.write_todos(todos)

st.title('Todo App')
st.subheader('Try using app')
st.text('this app is developed by python')

for index, todo in enumerate(todos):
	checkout = st.checkbox(todo, key=todo)
	if checkout:
		todos.pop(index)
		functions.write_todos(todos)
		del st.session_state[todo]
		st.rerun()

st.text_input(label='', placeholder='add a todo list...', on_change=add_todo,
              key='new_todo')

st.session_state