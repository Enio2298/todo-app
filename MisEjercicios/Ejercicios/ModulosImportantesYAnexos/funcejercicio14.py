Valmin = 0
Valmax = 100
def temperature(x):
    if x <= Valmin:
        return "Solido"
    elif Valmin< x <Valmax:
        return "Liquido"
    elif x >= Valmax:
        return "Vapor"