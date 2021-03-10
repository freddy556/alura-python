import cria_arquivo
import jogos
import os

def arquivo():
    resp = ""
    char = ""
    condicional = False
    menu()


    opt = input("Escolha uma opção: ")

    if(opt == "1"):
        arquivo = open("palavras.txt", "w", encoding="iso-8859-1")
        word = input("Digite a primeira palavra a constar no arquivo: ")
        arquivo.write(word)
        arquivo.write('\n')
        arquivo.close()
        print("Arquivo criado com sucesso! Retorne ao menu e selecione"
              " a opção 3 para adicionar mais palavras")
        print("")
        print("Pressione v para retornar ao menu de arquivo")
        char = input("")
        while(condicional != True):
            if(char == 'v' or char == 'V'):
                cria_arquivo.arquivo()
                condicional = True
                os.system('cls')
            else:
                print("Opção inválida!")
                char = input("")

    elif(opt == "2"):
        arquivo = open("palavras.txt", "r", encoding="iso-8859-1")
        for line in arquivo:
            print(line)
        arquivo.close()
        print("Pressione v para retornar ao menu de arquivo")
        char = input("")
        while (condicional != True):
            if (char == 'v' or char == 'V'):
                cria_arquivo.arquivo()
                condicional = True
                os.system('cls')
            else:
                print("Opção inválida!")
                char = input("")
    elif(opt == "3"):
        while(resp != "Nao".upper()):
            resp = input("Deseja adicionar palavra? Sim/Nao")
            resp.upper().strip()
            arquivo = open("palavras.txt", "a", encoding="iso-8859-1")
            if(resp == "Sim" or resp == "SIM" or resp == "S" or resp == "s"):
                add = input("Digite uma palavra: ")
                arquivo.write(add)
                arquivo.write('\n')
            elif(resp == "Nao" or resp == "NAO" or resp == "N" or resp == "n"):
                arquivo.close()
                print("Arquivo fechado!")
                print("Pressione v para retornar ao menu de arquivo")
                char = input("")
                while (condicional != True):
                    if (char == 'v' or char == 'V'):
                        cria_arquivo.arquivo()
                        condicional = True
                        os.system('cls')
                    else:
                        print("Opção inválida!")
                        char = input("")
            else:
                print("Opção inválida! Digite Sim ou Nao")
        arquivo.close()
    elif(opt == "4"):
        os.system('cls')
        jogos.escolhe_jogo()
    else:
        print("opção inválida!")
        char = input("")




def menu():

    print("************************************************")
    print("************************************************")
    print("***** Criação de arquivo de palavras ***********")
    print("************************************************")
    print("************************************************")
    print("***** 1 - Criar Arquivo ************************")
    print("************************************************")
    print("***** 2 - Exibir conteudo do Arquivo ***********")
    print("************************************************")
    print("***** 3 - Adicionar Itens ao Arquivo ***********")
    print("************************************************")
    print("***** 4 - Voltar ao menu ***********************")
    print("************************************************")
    print("************************************************")
    print("************************************************")


if(__name__ == "__main__"):
    arquivo()




