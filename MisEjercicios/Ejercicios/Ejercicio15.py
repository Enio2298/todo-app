import random

valinf = int(input('Introduce el valor mínimo del intervalo: '))
valsup = int(input('Introduce el valor superior: '))

valor_final = random.randint(valinf, valsup)

print(f'El valor aleatorio es: {valor_final}')

