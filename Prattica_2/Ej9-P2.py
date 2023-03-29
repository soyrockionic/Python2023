tabla = {"aeioulnrst":1,"dg":2,"bcmp":3,"fhvwy":4,"k":5,"jx":8,"qz":10}

pal = input("Ingrese una palabra ")

print(f"Valor de '{pal}' : {sum([tabla[clave] for letra in pal for clave in tabla if letra in clave])}")