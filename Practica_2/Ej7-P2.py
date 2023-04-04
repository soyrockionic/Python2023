import re

frase = """
El salario promedio de un hombre en Argentina es de $60.000, mientras que
el de una mujer es de $45.000. Además, las mujeres tienen menos
posibilidades de acceder a puestos de liderazgo en las empresas.
"""

# Identifico mayúsculas y minúsculas
mayusculas = [letra for letra in frase if letra.isupper()]
minusculas = [palabra.lower() for palabra in frase.split() if palabra.islower()]

# Identifico caracteres que no son letras
no_letras = re.findall(r'[^a-zA-Z\s]', frase)

# Cuento cantidad de palabras
palabras = len(frase.split())

print("Mayusculas:", mayusculas)
print("Minusculas:", minusculas)
print("Caracteres no letras:", no_letras)
print("Cantidad de palabras:", palabras)