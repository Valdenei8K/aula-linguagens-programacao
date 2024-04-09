#include <iostream>
#include <string>
using namespace std;

int main() {
    string nomeMarido, sobrenomeMarido,nomeEsposa,sobrenomeEsposa,sobrenome_novo_da_esposa;

    // Solicita o nome e sobrenome do usuário
    cout << "Digite seu nome do Marido: ";
    cin >> nomeMarido;
    cout << "Digite seu nome da Esposa: ";
    cin >> nomeEsposa;
    cout << "Digite sobrenome do Marido: ";
    cin >> sobrenomeMarido;
     cout << "Digite sobrenome da Esposa: ";
    cin >> sobrenomeEsposa;
    sobrenome_novo_da_esposa=sobrenomeMarido;
    // Imprime o sobrenome em letras maiúsculas seguido pela primeira letra do nome
    cout << nomeEsposa << ", " << sobrenome_novo_da_esposa << endl;

    return 0;
}
