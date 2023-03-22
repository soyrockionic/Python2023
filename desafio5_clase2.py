print("*"*30)
pelis_harry = {}
tmp = int(input("Ingrese duracion "))
while tmp != 0 :
    nombre = input("Ingrese nombre de la pelicula ")
    pelis_harry[nombre] = tmp
    tmp = int(input("Ingrese duracion "))
print("*"*30)
print(pelis_harry)

print("*"*30)
suma = 0
for i in pelis_harry :
    suma = suma + pelis_harry[i]
print(f"Promedio {suma / len(pelis_harry)}")

print("*"*30)
promedio = suma / len(pelis_harry)
mayor_promedio = [(i,pelis_harry[i]) for i in pelis_harry if pelis_harry [i] > promedio]
print(mayor_promedio)