#Calcular factoriales de un numero
num = int(input("Numero para factorial "))
factorial = 1
if num < 0:
    print<("Factorial no definido para numeros negativos")
else:
    for i in range(1, num + 1):
        factorial *= i
    print("El factorial de", num, "es", factorial)
#Hola Mundo #7
