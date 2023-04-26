try:
    ancho = float(input("Da la base: "))
    alto = float(input("Da la altura: "))

    if ancho == alto:
        exit("Eso es un cuadrado")

    area = ancho*alto
    print(area)
except ValueError:
    print("Introduce le valor como un número.")