dist = int(input("Qual a distância da viagem?: ").strip())
valor1 = 0.50
valor2 = 0.45

if dist <= 200:
    print("Valor por km: R${:.2F}".format(valor1))
    print("O valor da passagem é de R${:.2f}.".format(dist * valor1))
else:
    print("Valor por km: R${:.2F}".format(valor2))
    print("O valor da passagem é de R${:.2f}.".format(dist * valor2))
