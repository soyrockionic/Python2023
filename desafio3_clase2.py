print("*"*30)
pelis_harry = []
tmp = int(input("Ingrese duracion "))
while tmp != 0 :
    nombre = input("Ingrese nombre de la pelicula ")
    pelis_harry.append([nombre,tmp])
    tmp = int(input("Ingrese duracion "))
print("*"*30)
print(pelis_harry)

if len(pelis_harry) > 0 :
    print("*"*30)
    suma = 0
    for i in pelis_harry :
        suma = suma + i[1]
    print(f"Promedio {suma / len(pelis_harry)}")

if len(pelis_harry) > 0 :
    print("*"*30)
    promedio = suma / len(pelis_harry)
    cont = 0
    for i in pelis_harry :
        if(i[1] > promedio):
            cont = cont + 1
    print(f"Cantidad de pelis que duran mas que el promedio {cont}")