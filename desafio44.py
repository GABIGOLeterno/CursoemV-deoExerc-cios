while True:
    print("\033[1;4;33m{:=^40}\033[m".format(" LOJAS NA SUA TOBA "))
    valor = float(input("Valor do produto: R$").strip())
    taxa1 = "10%"
    taxa2 = "5%"
    taxa4 = "20%"
    desc1 = valor * 0.90
    desc2 = valor * 0.95
    juros = valor * 1.20
    print('''Forma de pagamento:
    [1] À VISTA DINHEIRO/CHEQUE;
    [2] À VISTA CARTÃO;
    [3] CARTÃO ATÉ 2X;
    [4] CARTÃO 3X OU MAIS.'''
          )
    pag = int(input("Forma de pagamento desejada: ").strip())

    if pag == 1:
        print('''\033[1;7;40mPagando-se à vista em dinheiro/cheque,\033[m 
\033[1;7;40mhá desconto de {} e o valor total é de R${:.2f}.\033[m'''.format(taxa1, desc1))
    elif pag == 2:
        print('''Pagando-se à vista em cartão,
há desconto de {} e o valor total é de R${:.2f}.'''.format(taxa2, desc2))
    elif pag == 3:
        parcelas = int(input("Número de parcelas: ").strip())
        while True:
            if parcelas in range(1, 3):
                print('''Pagando-se no cartão em {} vezes,
as parcelas são de R${:.2f}, no valor total de R${:.2f}.'''.format(parcelas, valor/parcelas, valor))
                break
            else:
                print("Opção inválida.")
                parcelas = int(input("Número de parcelas: ").strip())
    elif pag == 4:
        parcelas = int(input("Número de parcelas: ").strip())
        print('''Pagando-se no cartão em {} vezes, a parcela é de {:.2f},
há juros de {} e o valor total é de R${:.2f}.'''.format(parcelas, juros/parcelas, taxa4, juros))
    else:
        print("Opção inválida.")
    print("Obrigado.")
    print(" ")
