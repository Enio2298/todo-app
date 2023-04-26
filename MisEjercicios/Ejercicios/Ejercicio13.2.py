def func(nombres):
    nom = nombres.split(',')
    numero =len(nom)
    return numero
lista = input('Introduce los nombres de tus amigos, sin comas ni separaciones: ')
fin = func(lista)
print(fin)
