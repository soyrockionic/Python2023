import csv

with open('log_catedras.csv',encoding='utf-8') as arch:
    csv_reader = csv.reader(arch, delimiter=',')
    enc, data = next(csv_reader), list(csv_reader)

def respondieron_turno_mañana():
    users = []
    
    users = list(filter(lambda user: user[3] == "Cuestionario: Repaso clase 2 - Turno mañana" and 
                                     user[4] == "Ha comenzado el intento" and 
                                     user[6].startswith("163.10"), data))
    return users

r = respondieron_turno_mañana()

print("-"*26)
print(f"{enc[2]:<15}  {enc[0]}")
print("-"*26)
for u in r:
   v = u[0].split(',')
   print(f"{u[2]:<15} {v[1]}")