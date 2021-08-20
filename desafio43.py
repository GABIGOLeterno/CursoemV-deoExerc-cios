while True:
    peso = float(input("Peso em kg: ").strip())
    altura = float(input("Altura em metros: ").strip())
    imc = peso / (altura ** 2)

    print("Seu IMC é {:.2f} que é considerado".format(imc), end=' ')
    if imc < 18.5:
        print("ABAIXO DO PESO genérico.")
    elif imc <= 25:
        print("PESO IDEAL genérico.")
    elif imc <= 30:
        print("SOBREPESO genérico.")
    elif imc <= 40:
        print("OBESIDADE genérica.")
    else:
        print("OBESIDADE MÓRBIDA genérica.")
