import PySimpleGUI as sg
import csv

def start():

    try:
        # Abre el archivo CSV
        with open('netflix_titles.csv', "r", encoding='utf-8') as archivo:
            arch = csv.reader(archivo, delimiter=',')
            encabezado, data = next(arch), list(arch)
    
        # Selecciona solo las columnas que deseas mostrar
        data = [[row[0], row[2], row[3]] for row in data if row[1] == "Movie" and row[5] == "Argentina"]

        # Crea una lista de encabezados para la tabla
        headers = [encabezado[0], encabezado[2], encabezado[3]]

        # Crea un diseño para la ventana
        layout = [
            [sg.Table(values=data,
                  headings=headers,
                  max_col_width=25,
                  auto_size_columns=True,
                  justification='left',
                  num_rows=min(25, len(data)))]
        ]
    except:
        layout = [
              [sg.Text('¡Ups! Algo ocurrió. No se pudo cargar la información.',font=('Helvetica',10)),sg.Button('Ok')]
             ]

    return layout

# Crea una instancia de la ventana
window = sg.Window('Producciones argentinas en Netflix', start())

while True:

    # Muestra la ventana y espera a que el usuario la cierre
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'Ok':
        break

# Cierra la ventana
window.close()