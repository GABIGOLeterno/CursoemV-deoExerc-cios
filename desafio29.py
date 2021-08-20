while True:
    velo = float(input("Qual a velocidade do seu carro?: ").strip())
    limite = 70
    multa = 7.00

    if velo > limite:
        print("Você foi multado em por estar {:.2f}km acima da velocidade limite.".format(velo - limite))
        print("O valor da multa é de R${:.2f}.".format(float((velo - limite) * multa)))
    else:
        print("Tenha um boa viagem!")