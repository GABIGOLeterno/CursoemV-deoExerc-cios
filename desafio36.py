while True:
    emp = float(input("Qual o valor do empréstimo?: ").strip())
    sal = float(input("Qual o valor do seu salário? ").strip())
    anos = float(input("Pagamento será em quantos anos? ").strip())
    prest = emp/( anos * 12 )
    risco = 0.30
    if prest < sal * risco:
        print("Empréstimo \033[1;34mAPROVADO\033[m no valor total de \033[4mR${:.2f}\033[m, \033[4mR${:.2f}/mês\033[m em \033[4m{:.2f} anos\033[m.".format(emp, prest, anos))
    else:
        print("Empréstimo \033[;31mNÃO APROVADO\033[m.")
