nome = input("Digite seu nome: ").strip().title()
nome2 = nome.split()
print("Muito prazer em te conhecer, {}!".format(nome))
print("Seu primeiro nome é {}.".format(nome2[0]))
print("Seu último nome é {}.".format(nome2[len(nome2)-1]))
print(len(nome2))
