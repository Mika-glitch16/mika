matriz = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]


#uma forma de fzr 
print(matriz)
print(matriz[1][1])

for linha in matriz:
    for valor in linha:
        print(valor)




#outra forma de fzr 
for i in range(len(matriz)):
    for j in range(len(matriz[1])):
        print("linha", 1,"coluna",j,"->valor:",matriz[i][j])