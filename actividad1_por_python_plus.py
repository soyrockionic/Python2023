import csv

with open('log_catedras.csv',encoding='utf-8') as arch:
    csv_reader = csv.reader(arch, delimiter=',')
    enc, data = next(csv_reader), list(csv_reader)
arch.close()

def respondieron_turno_mañana():
    users = []
    for user in data:
        if(user[3] == "Cuestionario: Repaso clase 2 - Turno mañana"):
            if(user[4] == "Ha comenzado el intento"):
                if(user[6].startswith("163.10")):
                    users.append(user)
    return users

r = respondieron_turno_mañana()

print("-"*26)
print(f"{enc[2]:<15}  {enc[0]}")
print("-"*26)
for u in r:
   v = u[0].split(',')
   print(f"{u[2]:<15} {v[1]}")