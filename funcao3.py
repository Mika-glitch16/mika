def e_par(numero):                                                 #parametro é oq ta dentro da função, indice é  oq ta dentro lista
    return numero % 2 == 0

numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for numero in numeros: 
    if e_par(numero) : 
        print(numero, "é par")
    else: 
        print(numero, "é impar")