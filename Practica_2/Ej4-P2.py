evaluar = """ titulo: Experiences in Developing a Distributed Agent-based
Modeling Toolkit with Python
resumen: Distributed agent-based modeling (ABM) on high-performance
computing resources provides the promise of capturing unprecedented details
of large-scale complex systems. However, the specialized knowledge required
for developing such ABMs creates barriers to wider adoption and utilization.
Here we present our experiences in developing an initial implementation of
Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High
Performance Computing (Repast HPC), to identify the key elements of a useful
distributed ABM toolkit. We leverage the Numba, NumPy, and PyTorch packages
and the Python C-API to create a scalable modeling system that can exploit
the largest HPC resources and emerging computing architectures.
"""

titulo, resumen = evaluar.split("titulo: ", 1)
resumen = resumen.split("resumen: ")[1].strip()

# Verificar que el título no tenga más de 10 palabras
if len(titulo.split()) >= 10:
    print("El titulo no puede tener mas de 10 palabras.")
else:
    print("- Titulo ok")
    # Verificar cada oración del resumen según el número de palabras
    resumen_dividido = resumen.split(".")
    facil = 0
    aceptable = 0
    dificil = 0
    muy_dificil = 0
    for oracion in resumen_dividido:
        num_palabras = len(oracion.split())
        if num_palabras >=1 and num_palabras <= 12:
            facil += 1
        elif num_palabras >= 13 and num_palabras <= 17:
            aceptable += 1
        elif num_palabras >= 18 and num_palabras <= 25:
            dificil += 1
        elif num_palabras >= 26:
            muy_dificil += 1
    
# Imprimir las cantidades de oraciones por categoría de dificultad
print(f"- Fáciles de leer: {facil},", end=" ")
print(f" aceptables para leer: {aceptable},", end=" ")
print(f" difíciles de leer: {dificil},", end=" ")
print(f" muy difíciles de leer: {muy_dificil}")