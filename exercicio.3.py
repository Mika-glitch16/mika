num = [4,7,9,11,28,35,46,55]         #um jeito

for i in num:
    par = num % 2 == 0
    print(num, "é par?", par)



#outro jeito

    for i in num: 
        if i % 2 == 0:
         print(num, "é par?", par)
        else: 
           print(num, "é impar")