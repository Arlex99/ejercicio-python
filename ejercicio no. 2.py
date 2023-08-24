def es_palindromo(cadena):
    cadena_limpia = ''.join(c for c in cadena if c.isalnum()).lower()
    return cadena_limpia == cadena_limpia[::-1]

entrada_usuario = input("Ingrese una palabra o frase: ")

if es_palindromo(entrada_usuario):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")
