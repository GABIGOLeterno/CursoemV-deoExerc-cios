import random
from time import sleep
while True:
    print("Vou pensar em um número de 0 a 5. Tente adivinhar, fdp!!")
    num = int(input("Em qual número eu pensei?: ".strip()))
    if num in range(0,6):
        print("PROCESSANDO...")
        sleep(1)
        numpc = random.randint(0, 5) # Sorteio do PC
        if numpc == num:
            print("Acertou, mizerávi!")
        else:
            print("Errou! Eu pensei no {}, babaca.".format(numpc))
