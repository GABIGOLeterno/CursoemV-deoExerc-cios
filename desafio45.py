import random
from time import sleep
while True:
    print("--" * 11)
    jogo = ("Pedra", "Papel", "Tesoura")
    print('''PEDRA PAPEL OU TESOURA!
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA'''
          )
    escolha = int(input("Jogada: ").strip().upper())
    if escolha >=1 and escolha <= 3:
        jogada = jogo[escolha - 1]
        pc = random.randint(0,2)
        pc2 = jogo[pc]
        print("JO")
        sleep(1)
        print("KEN")
        sleep(1)
        print("PO!!!")
        sleep(1)
        print("Você jogou {} e o PC jogou {}.".format(jogada, pc2))
        if jogada == pc2:
            print("DEU EMPATE!")
        elif jogada == "Pedra":
            if pc2 == "Papel":
                print("O PC ganhou!")
            else:
                print("Você ganhou!")
        elif jogada == "Papel":
            if pc2 == "Tesoura":
                print("O PC ganhou!")
            else:
                print("Você ganhou!")
        elif jogada == "Tesoura":
            if pc2 == "Pedra":
                print("O PC ganhou!")
            else:
                print("Você ganhou!")
    else:
        print("Jogada inválida.")
