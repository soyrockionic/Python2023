import pandas as pd

data_set = pd.read_csv('log_catedras.csv', encoding='utf-8')

def respondieron_turno_mañana():
    users = data_set.loc[(data_set['Contexto del evento'] == "Cuestionario: Repaso clase 2 - Turno mañana") & 
                         (data_set['Nombre evento'] == "Ha comenzado el intento") &
                         (data_set['Dirección IP'].str.startswith("163.10"))]
    return users

users = respondieron_turno_mañana()

print(users[['Usuario afectado', 'Hora']])