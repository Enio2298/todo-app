import glob
"""Muestra todos los archivos con la terminación
que indiques dependiendo de la carpeta que selecciones
solo se puede en carpetas del mismo orden o inferiores"""
myfiles = glob.glob("*.txt")
for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())