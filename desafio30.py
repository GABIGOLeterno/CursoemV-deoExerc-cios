while True:
    num = int(input("Digite um número: ").strip())
    if (num %  2) == 0:
        print("O número {} é par.".format(num))
    else:
        print("Seu número {} é ímpar.".format(num))