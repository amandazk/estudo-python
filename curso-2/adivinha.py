import random

def joga_adivinha():

    numero_secreto = random.randrange(1,101) 
    total_tentativas = 0
    pontos = 1000

    print("Níveis do jogo:")
    print("1 - Fácil\n2 - Médio\n3 - Difícil")

    nivel = int(input("Escolha o nível desejado: "))

    if(nivel == 1):
        total_tentativas = 10
    elif (nivel == 2):
        total_tentativas = 5
    else:
        total_tentativas = 3

    for tentativa_atual in range(1, total_tentativas + 1):
        print("Tentativa {} de {}".format(tentativa_atual, total_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1):
            print("Você deve digitar um número entre 1 e 100")
            continue #volta pro for

        acertou = numero_secreto == chute
        maior = chute > numero_secreto 
        menor = chute < numero_secreto

        if (acertou):
            print("Parabéns, você acertou. Seu pontos foram: {}".format(pontos))
            break
        else:
            if(maior):
                print("Ops, você errou. Seu chute foi maior do que o número secreto")
            elif(menor):
                print("Ops, você errou. Seu chute foi menor do que o número secreto")

        pontos_perdidos = abs(numero_secreto - chute) 
        pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if (__name__ == "__main__"):
    joga_adivinha()
