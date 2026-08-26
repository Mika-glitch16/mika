num = [10, 20, 30, 40, 50]
print(num)
print(num[0])
print(num[2])
print(num[4])
print(len(num)) #len() saber quantos elementos tem na lista


num.append(60) #adiciona um elemento na lista
print(num) 

num[3] = 99  #altera o valor
print(num)

num.remove(20)#remove o valor
print(num)