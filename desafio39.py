from datetime import date
while True:
    ano = int(input("Ano de nascimento: ").strip())

    atual = date.today().year
    idade = atual - ano
    alistamento = ano + 18
    atraso = atual - alistamento
    faltas = alistamento - atual

    print("Quem nasceu em {} tem {} anos em {}.".format(ano, idade, atual))

    if idade > 18:
        print("Você deveria ter se alistado em {}.".format(alistamento))
        print("Você está atrasado {} anos.".format(atraso))
    elif idade < 18:
        print("Você deverá se alistar em {}.".format(alistamento))
        if 18 - idade >= 2:
            print("Ainda faltam {} anos para o seu alistamento.".format(faltas))
        else:
            print("Ainda falta {} ano para o seu alistamento.".format(faltas))
    else:
        print("Você deve se alistar \033[1;31mIMEDIATAMENTE\033[m.")

    escolha = input("Quer continuar, aperte q, se não, aperte ENTER: ".strip())
    if escolha == "q":
        break
