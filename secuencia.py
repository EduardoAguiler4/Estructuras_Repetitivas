#Imprimir secuencia aritetica
inicio = int(input("Primer numero:"))
diferencia = int(input("Diferencia:"))
limite = int(input("Limite Maximo:"))
num = inicio
while True:
    print(num, end = " ")
    num += diferencia
    if num > limite:
        break
print("\nSecuencia aritmetica desde ", inicio, " hasta ",limite )