import math
#solicitar al ucuario#
base = float(input("ingrese la base del terreno"))
altura = float(input("ingrese la altura del terreno"))
altura_rectangulo =float(input("ingrese la altura del terreno rectangulo"))
triangulo =(base*altura)/2
rectangulo =base*altura_rectangulo
area_total = triangulo + rectangulo
print(f"el area total del terreno es: {area_total}") (f"m2")