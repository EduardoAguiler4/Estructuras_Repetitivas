#Sumar numeros ingresados, dar la media y terminar al ingresar negativo
suma = 0
contador = 0
while True:
    num = float(input("Ingrese un número (negativo para terminar): "))
    if num < 0:
        break
    suma += num
    contador += 1
    if contador > 0:
        media = suma / contador
        print(":", media)
    else:
        print("No se ingresaron positivos")
#Hola mundo #11
