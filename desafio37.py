while True:
    num = int(input("Digite um número: ").strip())
    print('''Você quer esse número em que formato?
[1]BINÁRIO
[2]OCTAL
[3]HEXADECIMAL'''
         )
    escolha = int(input("Digite o código da opção escolhida: ").strip())
    if escolha == 1:
        print("\033[1;34mO valor de {} em binário é {}.\033[m".format(num, bin(num)[2:]))
    elif escolha == 2:
        print("\033[1;34mO valor de {} em octal é {}.\033[m".format(num, oct(num)[2:]))
    elif escolha == 3:
        print("\033[1;34mO valor de {} em hexadecialm é {}.\033[m".format(num, hex(num)[2:]))
    else:
        print("\033[1;31mOpção inválida. Repita o processo.\033[m")
