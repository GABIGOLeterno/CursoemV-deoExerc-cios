while True:
    quant = int(input("Quantas avaliações foram?: "))
    ls = []

    for n in range(quant):
        notas = int(input("Digite a nota: ").strip())
        ls.append(notas)
    media = sum(ls)/len(ls)
    print("Suas notas foram:", ls)
    if media >= 7.0:
        print("Parabéns, você foi aprovado com média {:.1f}.".format(media))
    elif 7.0 > media >= 5.0:
        print("Opa, mais uma etapa. Você ficou de recuperação com a média {:.1f}.".format(media))
    else:
        print("Você foi reprovado com média {:.1f}.".format(media))

    escolha = input("Quer continuar, aperte q, se não, aperte ENTER: ".strip())
    if escolha == "q":
        break
