nombres = ''' 'Agustin', 'Alan', 'Andrés', 'Ariadna', 'Bautista', 'CAROLINA', 'CESAR',
'David','Diego', 'Dolores', 'DYLAN', 'ELIANA', 'Emanuel', 'Fabián', 'Facundo',
'Francsica', 'FEDERICO', 'Fernanda', 'GONZALO', 'Gregorio', 'Ignacio', 'Jonathan',
'Joaquina', 'Jorge','JOSE', 'Javier', 'Joaquín' , 'Julian', 'Julieta', 'Luciana',
'LAUTARO', 'Leonel', 'Luisa', 'Luis', 'Marcos', 'María', 'MATEO', 'Matias',
'Nicolás', 'Nancy', 'Noelia', 'Pablo', 'Priscila', 'Sabrina', 'Tomás', 'Ulises',
'Yanina' '''

notas_1 = [81, 60, 72, 24, 15, 91, 12, 70, 29, 42, 16, 3, 35, 67, 10, 57, 11, 69,
12, 77, 13, 86, 48, 65, 51, 41, 87, 43, 10, 87, 91, 15, 44,
85, 73, 37, 42, 95, 18, 7, 74, 60, 9, 65, 93, 63, 74]

notas_2 = [30, 95, 28, 84, 84, 43, 66, 51, 4, 11, 58, 10, 13, 34, 96, 71, 86, 37,
64, 13, 8, 87, 14, 14, 49, 27, 55, 69, 77, 59, 57, 40, 96, 24, 30, 73,
95, 19, 47, 15, 31, 39, 15, 74, 33, 57, 1]

def estudiantes_y_sus_notas():
    dicc = {}
    names = nombres.replace("'","").replace(" ","").replace("\n","").split(",")
    for n, v1, v2 in zip(names, notas_1, notas_2):
        dicc[n] = [v1, v2]
    return dicc
    
def promedio_de_cada_estudiante(est):
    promedios = dict(map(lambda x: (x[0], sum(x[1]) / len(x[1])), est.items()))    
    return promedios

def promedio_general(est):
    return (lambda x: sum(x.values()) / len(x))(promedio_de_cada_estudiante(est))

def estudiante_con_promedio_mas_alto(est):
    promedios = promedio_de_cada_estudiante(est)
    estudiante_mayor_prom, nota = max(promedios.items(), key=lambda x: x[1])
    return estudiante_mayor_prom + " con promedio: " + str(nota)

def estudiante_con_nota_mas_baja(est):
    estudiante_menor_nota, nota = min(est.items(), key=lambda x: min(x[1]))
    return estudiante_menor_nota + " con nota: " + str(min(nota))


estudiantes = estudiantes_y_sus_notas()

print()
print("***** Todos los estudiantes y su promedio *****")
print(promedio_de_cada_estudiante(estudiantes))

print()
print(f"Promedio general {promedio_general(estudiantes):.2f}")

print()
print(f"Estudiante con mayor promedio {estudiante_con_promedio_mas_alto(estudiantes)}")

print()
print(f"Estudiante con la nota mas baja {estudiante_con_nota_mas_baja(estudiantes)}")