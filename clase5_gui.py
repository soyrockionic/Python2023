import PySimpleGUI as sg
import csv

archivo = open('netflix_titles.csv', "r",encoding='utf-8')
arch = csv.reader(archivo, delimiter=',')

enc = next(arch)

def producciones(pelis):
    for peli in arch:
        if "2019" == peli[7] and "Argentina" == peli[5]:
            pelis = pelis + f"{peli[2]:<45} {peli[1]:<4}" + "\n"
    return pelis

titles = "Producciones argentinas 2019 - Netflix"
pelis = ""
layout = [[sg.Text(titles + "\n" + "-"*72)], [sg.Text(producciones(pelis))], [sg.Button("Salir")]]

archivo.close()

window = sg.Window("Informe - Netflix", layout, size=(600,450), margins=(130,60))

event, values = window.read()

window.close()