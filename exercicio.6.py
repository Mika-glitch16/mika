produtos_preços = [14.90, 15.76, 29.80, 32.99, 180.77, 19.98, 20.00]
print("produtos_preços")
contador_acima_20 =0
total = 0

for i in produtos_preços:  
    if i >= 20:
      print(i, "produtos acima de 20$: ")
else: 
    print(i, "produtos abaixo de 20$: ")

    for preco in produtos_preços:
       total = total + preco
       if preco > 20.00: 
          contador_acima_20 = contador_acima_20 + 1

print("produtos acima de 20.00", contador_acima_20 )
print("valor total: ", total)
