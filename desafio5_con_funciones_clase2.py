def ingreso_pelis():
    pelis = {}
    tmp = int(input("Ingrese duracion "))
    while tmp != 0 :
        nombre = input("Ingrese nombre de la pelicula ")
        pelis[nombre] = tmp
        tmp = int(input("Ingrese duracion "))
    return pelis

def promedio(pelis_harry):
    return sum(pelis_harry[i] for i in pelis_harry)

def mayor_promedio(pelis_harry):
    return [(i,pelis_harry[i]) for i in pelis_harry if pelis_harry [i] > promedio(pelis_harry)]

print("*"*30)
pelis_harry = ingreso_pelis()
print(pelis_harry)

print("*"*30)
print(f"Promedio {promedio(pelis_harry)}")

print("*"*30)
print(mayor_promedio(pelis_harry))