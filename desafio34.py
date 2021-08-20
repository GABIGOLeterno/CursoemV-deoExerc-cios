while True:
    sal = float(input("Digite o seu salário bruto:R$ ").strip())
    base = 1250.00
    dez = 1.1
    quinze = 1.15

    if sal <= base:
        print("Seu salário é de R${:.2F}.".format(sal * quinze))
    else:
        print("Seu salário é de R${:.2F}.".format(sal * dez))
