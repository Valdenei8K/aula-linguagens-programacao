

notas = []
soma = 0
media = 0

for i in range(len(notas)):
    notas[i] = int(input("Digite a " + str(i+1) + "º nota: "))

for i in range(len(notas)):
    soma=notas[i] + soma
    
media=soma/len(notas)



print(media)
if(media>=7):
    print("aluno aprovado")
else:
        print("Aluno reprovado")
    
