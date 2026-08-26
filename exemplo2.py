par = 0
impar = 0

for i in range(1,11):
    numero = int(input("Digite um numero: "))
    
    if numero % 2 == 0:
     par = par + 1

    else:
     impar = impar + 1 

    
print("Quantidade de numeros pares: ", par)
print("Quantidade de numeros impares: ", impar)


