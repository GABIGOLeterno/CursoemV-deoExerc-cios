from datetime import date
while True:
    ano = int(input("Ano de nascimento: ").strip())
    atual = date.today().year
    idade = atual - ano
    print("Idade: {} anos.".format(idade))
    if idade < 9:
        print("Categoria: \033[1;33mMIRIM\033[m.")
    elif 14 > idade >= 9:
        print("Categoria: \033[1;34mINFANTIL\033[m.")
    elif 19 > idade >= 14:
        print("Categoria: \033[1;35mJÚNIOR\033[m.")
    elif 25 > idade >= 19:
        print("Categoria: \033[1;36mSÊNIOR\033[m.")
    else:
        print("Categoria: \033[1;37mMASTER\033[m.")

    escolha = input("Aperte 'q' para sair, aperter enter para seguir: ")
    if escolha == "q":
        break
