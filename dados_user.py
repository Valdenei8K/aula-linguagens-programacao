#faça um programa em python com uma lista chamda"dados"
#a lista tera 4 elementos, o primeiro deve ser o nome 
#do usuario, o segundo deve ser a idade, o terceiro a 
#altura e o ultimo o bairro
#imprima a lista no final


dados = []
campos = ['Nome', 'Idade', 'Altura', 'Bairro']

dados[0] = input("Digite seu nome: ") 
dados[1] = int(input("Digite sua idade: "))  
dados[2] = float(input("Digite sua altura (em metros): "))  
dados[3] = input("Digite seu bairro: ")  


print("Lista de dados:")
print("Formulário:")
for i in range(len(dados)):
    print(f"{campos[i]}: {dados[i]}")
