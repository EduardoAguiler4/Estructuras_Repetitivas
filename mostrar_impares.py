#Mostrar numeros impares
N = int(input("Numero positivo: "))
i = 1
while True:
    if i % 2 != 0:
        print(i, end = " ")
    i += 1
    if i > N:
        break
print("\nFin. se mostraron los numeros impares hasta", N)   
#Hola Mundo #8
