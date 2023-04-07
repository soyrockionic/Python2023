import csv

archivo = open('netflix_titles.csv', "r",encoding='utf-8')
csvreader = csv.reader(archivo, delimiter=',')

encabezado = next(csvreader)

print()
print(f"{encabezado[2]:<45}  {encabezado[3]}")
print(f"{'-'*45}  {'-'*33}")

#for linea in csvreader:
    #if linea[1] == "Movie" and linea[5] == "Argentina":
        #print(f"{linea[2]:<45}  {linea[3]}")

shows_ar = filter(lambda x: x[5] == "Argentina" and x[1] == "Movie", csvreader)
for elem in shows_ar:
    print(f"{elem[2]:<45}  {elem[3]}")

archivo.close()