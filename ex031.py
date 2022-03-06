d = float(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {} km".format(d))
preço = d * 0.50 if d <= 200 else d * 0.45
print("O preço da sua passagem será de R${:.2f}".format(preço))

'''if d <= 200:
    preço = d * 0.50
else:
    preço = d * 0.45'''

