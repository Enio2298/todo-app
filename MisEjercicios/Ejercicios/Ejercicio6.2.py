nuevo = input("Introduce nuevo miembro: ")
with open(r"C:\Users\enio2\Downloads\Cursos\Python\members.txt", "r") as file:
    miembros_ya = file.readlines()
    file.close()
miembros_ya.append(nuevo + "\n")
file = open(r"C:\Users\enio2\Downloads\Cursos\Python\members.txt", "w")
miembros_ya = file.writelines(miembros_ya)
file.close()