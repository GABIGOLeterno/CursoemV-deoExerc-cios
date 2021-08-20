while True:
    print("Qual valor é maior?")
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    if num1 > num2:
        print("O \033[1;4;36mPRIMEIRO\033[m valor é maior.")
    elif num2 > num1:
        print("O \033[1;4;35mSEGUNDO\033[m valor é maior.")
    else:
        print("Os valores são iguais.")

    escolha = input("Quer continuar, aperte q, se não, aperte ENTER: ".strip())
    if escolha == "q":
        break
