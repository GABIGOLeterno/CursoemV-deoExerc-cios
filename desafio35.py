print("Analisador de Triângulos")
while True:
    l1 = int(input("Digite o valor do segmento 1: ").strip())
    l2 = int(input("Digite o valor do segmento 2: ").strip())
    l3 = int(input("Digite o valor do segmento 3: ").strip())
    if l1 < l2 + l3 and l2 < l3 + l1 and l3 < l1 + l2:
        print("Segmentos {},{} e {} formam um triângulo.".format(l1, l2, l3))
    else:
        print("Segmentos {},{} e {} não formam um triângulo.".format(l1, l2, l3))
