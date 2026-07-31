#Ver si las letras son vocales o consonantes
while True:
    letra = input("Ingrese una letra (espacio termina): ")
    if letra == " ":
        break
    letra = letra.lower()
    if letra in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
print("Programa Finalizado")

    