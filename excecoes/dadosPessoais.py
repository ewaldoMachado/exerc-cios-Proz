def dadosPessoais():
    dados = True
    while (dados == True):
        print("Insira seu nome")
        nome = input()
        print("Insira sua data nascimento")

        try:
            ano = int(input())
            if (ano < 1922) or (ano > 2021):
                dados = False
                print("ano ou caractere invalido")
                dadosPessoais()

            else :
                idade = 2022 - ano
                print(nome," ", idade, " anos de idade")
                break
            
        except:
            print("Erro. Tente novamente")

dadosPessoais()