
 # Representação inicial do tabuleiro
tabuleiro = [[" "]*3 for _ in range(3)]

def exibir_menu():
    print("----------------------------------")
    print("Seja bem-vindo ao jogo da velha!")
    print("----------------------------------")

def imprimir_tabuleiro():
    for linha in tabuleiro:
        print("|".join(linha))
        print("-----")

def marca_posicao(jogador, linha, coluna):
    if tabuleiro[linha][coluna] == " ":
        tabuleiro[linha][coluna] = jogador
        return True
    else:
        print("Posição inválida. Escolha outra.")
        return False

def main():
    exibir_menu()
    jogador_atual = "X"

    while True:
        imprimir_tabuleiro()
        linha, coluna = map(int, input(f"É a vez do jogador {jogador_atual}, em qual posição você deseja jogar? (linha coluna): ").split())
        
        if marca_posicao(jogador_atual, linha, coluna):
            with open("tabuleiro.txt", "w") as arquivo:
                for linha_tabuleiro in tabuleiro:
                    arquivo.write("|".join(linha_tabuleiro) + "\n")
                    arquivo.write("-----\n")
            
            if jogador_atual == "X":
                jogador_atual = "O"
            else:
                jogador_atual = "X"

# Rodando o jogo
main()
