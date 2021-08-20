print("Analisador de Triângulos")
while True:
    l1 = int(input("Digite o primeiro segmento: ").strip())
    l2 = int(input("Digite o segundo segmento: ").strip())
    l3 = int(input("Digite o terceiro segmento: ").strip())

    if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
        if l1 == l2 == l3:
            print("Segmentos {}, {} e {} formam um triângulo do tipo \033[32;40mEQUILÁTERO\033[m.".format(l1, l2, l3))
        elif l1 != l2 != l3:
            print(("Segmentos {}, {} e {} formam um triângulo do tipo \033[33;40mESCALENO\033[m.".format(l1, l2, l3)))
        else:
            print(("Segmentos {}, {} e {} formam um triângulo do tipo \033[34;40mISÓCELES\033[m.".format(l1, l2, l3)))
    else:
        print("Segmentos não podem formar um triângulo..")

    escolha = input("Digite 'q' para continuar, ou aperte ENTER para seguir: ").strip()
    if escolha == "q":
        break
