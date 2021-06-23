import forca
import adivinha

def escolhe_jogo():
    print("Escolha o seu jogo")
    print("1 - Forca\n2 - Adivinhação")

    jogo = int(input("Jogo escolhido: "))

    if (jogo == 1):
        print("Jogando Forca")
        forca.joga_forca()
    elif (jogo == 2):
        print("Jogando adivinhação")
        adivinha.joga_adivinha()

if (__name__ == "__main__"):
    escolhe_jogo()
