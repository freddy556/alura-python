import random
import os
import jogos





def jogar():
    
    mensagem_abertura()
    palavra_secreta = carrega_palavra()
    letras_certas = inicializa_letras_certas(palavra_secreta)
    letras_erradas = []



    enforcou = False
    acertou = False
    erros = 0

    print(letras_certas)


    #enquanto não enforcar o status continua como false, acertou só muda de status com o acerto da palavra
    while(not enforcou and not acertou):

        chute = pede_chute()
        if(chute in palavra_secreta):
            chute_correto(chute, letras_certas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
            print("A letra {} não faz parte da palavra!".format(chute))
            letras_erradas.append(chute)
            print("Letras erradas:", letras_erradas)


        enforcou = erros == 7
        letras_faltando = str(letras_certas.count('_'))
        print(letras_certas)
        g_over = int(letras_faltando)
        if(g_over > 0):
            print("Faltam {} letras".format(g_over))
        else:
            mensagem_win()
            char = input("")
            os.system('cls')
            jogos.escolhe_jogo()
        if(enforcou == True):
            mensagem_lose(palavra_secreta)
            char = input("")
            os.system('cls')
            jogos.escolhe_jogo()
    
def mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for line in arquivo:
        line = line.strip()
        palavras.append(line)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta



def inicializa_letras_certas(palavra):
    print("\nPalavra: ")
    return ["_" for letra in palavra]


def pede_chute():
    chute = input("Digite uma letra: ")
    chute = chute.strip().upper()
    return chute

def chute_correto(chute, letras_certas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_certas[index] = letra
        index += 1


def mensagem_win():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def mensagem_lose(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print("")



if(__name__ == "__main__"):
    jogar()