while True:
    with open("../Ejercicios/ModulosImportantesYAnexos/moneda8.txt", "r") as file:
        caras = file.readlines()
    cara = input("introduce aguila o sol: ")
    caras.append(cara+"\n")
    with open("../Ejercicios/ModulosImportantesYAnexos/moneda8.txt", "w") as file:
        file.writelines(caras)
    num_caras = caras.count("aguila\n")
    porcentaje = num_caras / len(caras)*100

    print(f"Porcentaje de aguilas: {porcentaje}%")

