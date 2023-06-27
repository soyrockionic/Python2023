import pandas as pd

archivo_log = "log_completo.csv"

def mi_funcion(datos, *args):
    # Filtro los datos por los argumentos proporcionados
    filtro = datos['Nombre completo del usuario'].isin(args)
    # Aplico groupby y obtengo el tamaño de cada grupo
    groupby_resultado = datos[filtro].groupby('Nombre completo del usuario').size()
    return groupby_resultado

datos_log = pd.read_csv(archivo_log)

resultado = mi_funcion(datos_log, "Hypno", "Butterfree", "Rhyhorn", "Slowpoke")

# Creo un DataFrame a partir del resultado y renombro la columna con lo recuentos 'Recuento'
tabla_resultado = pd.DataFrame(resultado, columns=['Recuento']).reset_index()

print(tabla_resultado)