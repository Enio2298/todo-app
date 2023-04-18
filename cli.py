#from functions import get_todos, write_todos
import functions
import time
now = time.strftime('%H:%M:%S, %d/%b/%Y')
while True:
    user_action = input("introduce add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        todos = functions.get_todos()
        todos.append(todo + "\n")
        functions.write_todos(todos)
    elif user_action.startswith('show'):
        todos = functions.get_todos()
        new_todos = []
        for item in todos:
            new_item = item.strip('\n')
            new_todos.append(new_item)
        for index, item in enumerate(new_todos):
            product = f"{index+1}.-{item}"
            print(product)
    elif user_action.startswith('edit'):
       try:
            number = int(user_action[5:])
            number = number - 1
            todos = functions.get_todos()
            new_todo = input("Introduce la nueva acción: ")
            todos[number] = new_todo + '\n'
            functions.write_todos(todos)
       except ValueError:
           print('Tu orden no es válida')
           continue
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            num = number-1
            act_eliminada = todos[num].strip()
            print('Actividad eliminada:', act_eliminada)
            todos.pop(num)
            functions.write_todos(todos)
        except IndexError:
            print('No hay una comida con ese número')
            continue
    elif user_action.startswith('exit'):
        break
    else:
        print('Comando no válido.')
print('Bye!')
