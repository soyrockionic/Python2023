import csv
import json

with open('netflix_titles.csv',encoding='utf-8') as archi_pelis:
    csv_reader = csv.reader(archi_pelis, delimiter=',')
    encabezado, data = next(csv_reader), list(csv_reader)

arch = open("pelis.txt", "w")
pelis = []
for linea in data:
    if(len(linea[5].split(",")) > 1):
        dicc = {}
        for e,p in zip(encabezado,linea):
            dicc[e] = p
        pelis.append(dicc)
json.dump(pelis, arch, indent=4)
arch.close()

por_pais = {}
for row in data:
    if '2019' in row[7]:
        if row[5] in por_pais:
            por_pais[row[5]] += 1
        else:
            por_pais[row[5]] = 1
top_5_paises = sorted(por_pais, key=por_pais.get, reverse=True)[:5]
print()
print(top_5_paises)

archi_pelis.close()