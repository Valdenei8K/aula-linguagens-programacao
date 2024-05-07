notas = []
soma = 0


while True:
    nota = int(input("Digite a nota (ou -1 para encerrar): "))
    if nota == -1:
        break 
    notas.append(nota)  


for nota in notas:
    soma += nota


media = soma / len(notas)


print("Média:", media)
if media >= 7:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
