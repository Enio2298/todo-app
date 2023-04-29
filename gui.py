import functions
import PySimpleGUI as sg
import time

sg.theme("BrightColors")

Hour = sg.Text("", key="Hour")
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo",
                         key="todo")
add_button = sg.Button('Add', size=10)
list_box = sg.Listbox(values=functions.get_todos(),
                      key='todos', enable_events=True,
                      size=[40,7])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

#button_labels = ["Close", "Apply"]
#Layout = []
#for bl in button_labels:
    #layout.append([sg.Button(bl)])
#[[sg.Button("Close")], [sg.Button("Apply"]]
#"""Se crea una lista llamada Layout, para cada
#etiqueta del botón, se creará un sg.Button,
#en la lista Layout"""

window = sg.Window('My To-Do App',
                   layout=[[Hour],
                       [label], [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica",13))
while True:
    event, values = window.read(timeout=10)
    """El timeout, hace que WhileLoop se aplica cada
    10 milisegundos, esto para que se actualice y de la
    hora cada 10 milisegundos"""
    window["Hour"].update(value=time.strftime('%H:%M:%S, %d/%b/%Y'))
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'].replace("\n", "") + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Introduce una acción", font=("Helvetica", 13))
        case 'todos':
            window["todo"].update(value=values["todos"][0])
        case "Complete":
            try:
                todo_to_complete = values["todos"][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window["todos"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Introduce una acción", font=("Helvetica", 13))
        case "Exit":
            break
        case sg.WIN_CLOSED:
            break

window.close()
