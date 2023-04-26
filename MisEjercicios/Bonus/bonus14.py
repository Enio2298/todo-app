from funcparse import parse
from funcconvert import convert

feet_inches = input("Enter feet and inches: ")

parsed = parse(feet_inches)

result = convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result} m")

if result < 1:
    print("Lo siento medio metro")
else:
    print("Adelante, perro")