matriz = [
     [5,7,9,8],
     [6,8,5,7],                                                       #situacao é pra qnd se tem uma decisao diferente mais com a msm variavel
     [4,6,5,6]
]

for linha in matriz:                       #primeiro loop 
      numero_aluno = 1     
      soma = 0 
      for nota in linha:                   #segundo loop
       soma = soma + matriz 
       media = soma/len(linha)

if media >= 6.0: 
        situacao = "Aprovado"
else: 
        situacao = "Reprovado"

numero_aluno += 1
print(f"Aluno {numero_aluno}: media{media:.2f}- {situacao}")
