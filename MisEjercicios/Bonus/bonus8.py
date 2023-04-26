fecha = input("Introduce la fecha de hoy: ")
humor = input("Cómo calificas el día del 1 al 10: ")
diario = input("Pequeño comentario al respecto:")

with open(f"../Ejercicios/ModulosImportantesYAnexos/{fecha}.txt", "w") as file:
    file.write(humor + "\n")
    file.write(diario)
