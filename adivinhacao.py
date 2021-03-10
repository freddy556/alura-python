import random


def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Advinhação!")
    print("********************************")

    numero_secreto = random.randrange(1, 101)
    rodada = 1
    total_tentativa = 0
    pontos = 0

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Dificil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_tentativa = 20
        pontos = 1000
    elif(nivel == 2):
        total_tentativa = 10
        pontos = 2000
    else:
        total_tentativa = 5
        pontos = 3000

    for rodada in range (1, total_tentativa+1):
        print("Tentativa {} de {}".format(rodada, total_tentativa))

        chute = input("Digite um número entre 1 e 100: ")

        chute_resp = int(chute)

        if(chute_resp <= 0 or chute_resp > 100):
            print("Número inválido, digite um número entre 1 e 100!")
            continue

        print("Você digitou ", chute)

        acertou = chute_resp == numero_secreto
        maior   = chute_resp > numero_secreto
        menor   = chute_resp < numero_secreto

        if (acertou):
            print("Você acertou! Você fez {} pontos".format(pontos))
            break
        else:
            if (maior):
                print("Errou! Seu chute foi maior que o número secreto")
            elif(menor):
                print("Errou! Seu chute foi menor que o número secreto")
            pontos_perdidos = abs(numero_secreto - chute_resp)
            pontos = pontos - pontos_perdidos




    print("Fim do jogo! {} era o número secreto".format(numero_secreto))

if(__name__ == "__main__"):
    jogar()
