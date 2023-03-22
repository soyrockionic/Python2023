def ingreso_pelis():
    pelis_harry = {}
    tmp = int(input("Ingrese duracion "))
    while tmp != 0 :
        nombre = input("Ingrese nombre de la pelicula ")
        pelis_harry[nombre] = tmp
        tmp = int(input("Ingrese duracion "))
    return pelis_harry

def promedio(pelis_harry):
    suma = 0
    for i in pelis_harry :
        suma = suma + pelis_harry[i]
    return suma / len(pelis_harry)

def mayor_promedio(pelis_harry):
    return [(i,pelis_harry[i]) for i in pelis_harry if pelis_harry [i] > promedio(pelis_harry)]

print("*"*30)
pelis_harry = ingreso_pelis()
print(pelis_harry)

print("*"*30)
print(f"Promedio {promedio(pelis_harry)}")

print("*"*30)
print(mayor_promedio(pelis_harry))