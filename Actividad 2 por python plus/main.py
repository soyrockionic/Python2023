import json, csv
import clases 
import random

def obtengo_datos(nombre_archivo):
    try:
        if nombre_archivo.endswith("json"):
            with open(nombre_archivo, "r") as archi:
                datos = json.load(archi)
        elif nombre_archivo.endswith("csv"):
            with open(nombre_archivo, "r") as archi:
                csvreader = csv.reader(archi, delimiter=',')
                linea1 = next(csvreader)
                linea2 = next(csvreader)
                datos = dict(zip(linea1, linea2))
        else:
            datos = {}
    except FileNotFoundError:
        print(f"El archivo '{nombre_archivo}' no se encontro.")
        datos = {}
    return datos


archivos = ["datos.json", "datos.csv"]
archi = random.choice(archivos)
datos_bandas = obtengo_datos(archi)

try:
    banda = clases.Banda(datos_bandas['nombre'], datos_bandas["genero"])
    lista = []
    cant_integrantes = int(datos_bandas["cant_integrantes"])
    lista = [input("Ingresa un integrante: ") for _ in range(cant_integrantes)]
    banda.integrantes = lista
    print(banda)
except KeyError:
    print("Error: Los datos de la banda estan incompletos o no se encontraron.")

print("FIN DEL PROGRAMA")