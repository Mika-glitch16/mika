matriz = [                                  # o primeiro loop separa primeiro por linha
    [6,7,5],                                # o segundo loop vai pegar o valor da coluna
    [10,98.67],                             # matrizes sao conjuntos de listas
    [65,78,90]
]

for linha in matriz:                            # primeiro loop
    for valor in linha:                         # segundo loop
        if valor % 2 == 0: 
            print(valor, "é par")
        else: 
            print(valor, "é impar")