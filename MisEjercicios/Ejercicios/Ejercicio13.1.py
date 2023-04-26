year_of_birth = int(input("Introduce tu año de nacimiento: "))
def func(year_of_birth, current_year=2023):
    edad = current_year - year_of_birth
    return edad
annos = func(year_of_birth)

if annos > 120:
    print("Debes estar muerto")
else:
    print("Hola")