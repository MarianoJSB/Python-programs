#Funcion para eliminar los espacios de la palabra ingresada
def eliminarEspacios(texto):
    vacio = ""
    for c in texto:
        if c != " ":
            vacio += c
    return vacio

#Funcion para invertir la palabra ingresada
def invertirPalabra(palabra):
    vacio = ""
    for c in palabra:
        vacio = c + vacio
    return vacio

#Funcion que devuelve un boolean dependiendo si es palindroma o no la palabra ingresada
def es_palidromo(texto):
    texto = eliminarEspacios(texto)
    reverse = invertirPalabra(texto)
    return texto.lower() == reverse.lower()

usuario = input("Enter a text to know if it is palindrome: ")
print(f'{usuario}', es_palidromo(f'{usuario}'))
