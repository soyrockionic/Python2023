import csv

with open('netflix_titles.csv', "r",encoding='utf-8') as archivo:
    arch = csv.reader(archivo, delimiter=',')
    encabezado, datos = next(arch), list(arch)

print()
print(f"{encabezado[2]:<45}  {encabezado[3]}")
print(f"{'-'*45}  {'-'*33}")

#for linea in datos:
    #if linea[1] == "Movie" and linea[5] == "Argentina":
        #print(f"{linea[2]:<45}  {linea[3]}")

shows_ar = filter(lambda x: x[5] == "Argentina" and x[1] == "Movie", datos)
for elem in shows_ar:
    print(f"{elem[2]:<45}  {elem[3]}")