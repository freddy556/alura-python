import forca
import adivinhacao
import cria_arquivo
import os




def escolhe_jogo():
    quit_status = False
    menu()
    jogo = int(input("Sua opção: "))

    if(jogo == 1):
        print("Forca selecionado!")
        os.system('cls')
        forca.jogar()
    elif(jogo == 2):
        print("Adivinhação selecionado!")
        os.system('cls')
        adivinhacao.jogar()
    elif(jogo == 3):
        print("Extras selecionado!")
        cria_arquivo.arquivo()
        os.system('cls')
    elif(jogo == 4):
        os.system('cls')
        print("Deseja mesmo sair? [S/N]")
        quit = input("Sua opção: ")
        while(quit_status == False):
            if(quit == "S" or quit == "s"):
                os.system('cls')
                print("Saindo do jogo.....")
                os.system('cls')
                quit_status = True
                break
            elif(quit == "N" or quit == "n"):
                os.system('cls')
                print("Retornando ao menu.....")
                os.system('cls')

                escolhe_jogo()
                quit_status = True


def menu():
    print("**************************************************")
    print("**************************************************")
    print("*************** MENU DE JOGOS ********************")
    print("**************************************************")
    print("**************************************************")
    print("******* 1 - Jogo da Forca ************************")
    print("**************************************************")
    print("******* 2 - Jogo da Adivinhação de número ********")
    print("**************************************************")
    print("******* 3 - Extras *******************************")
    print("**************************************************")
    print("******* 4 - Sair *********************************")
    print("**************************************************")
    print("**************************************************")

if(__name__ == "__main__"):
    escolhe_jogo()