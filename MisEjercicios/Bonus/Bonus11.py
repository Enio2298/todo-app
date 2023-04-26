def func():
    with open("../Ejercicios/ModulosImportantesYAnexos/Bonus11.txt", "r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]
    average = sum(values) / len(values)
    return average


average = func()
print(average)