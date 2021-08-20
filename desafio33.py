while True:
    num = str(input("Digite três valores: ").strip())
    num2 = num.split()
    if len(num2) == 3:
        maxi = max(num2)
        mini = min(num2)
        print("O valor máximo é {}.".format(maxi))
        print("O valor mínimo é {}.".format(mini))
