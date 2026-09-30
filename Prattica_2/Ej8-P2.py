def es_heterograma(texto):
    if not texto.strip():
        return False

    texto = texto.lower()
    
    letras = [caracter for caracter in texto if caracter.isalpha()]
    
    return len(letras) == len(set(letras))

texto = input("Ingrese una palabra o frase: ")
    
if es_heterograma(texto):
    print(f'"{texto}" SI es un heterograma.')
else:
    print(f'"{texto}" NO es un heterograma.')