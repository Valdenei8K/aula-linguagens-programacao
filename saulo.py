soma = 0
cont = 0
for i in range (0 , 10):
    nota = float (input('nota: '))
    cont = cont + 1
    soma = soma + nota
else:
    media = soma / cont

if media >= 7:
    print("Média", media)
    print("aprovado")
else:
    print("Média", media)
    print("reprovado")