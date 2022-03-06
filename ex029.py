vel = float(input("Qual é a velocidade atual do carro? "))
if vel > 80:
    print("MULTADO! você excedeu o limite permitido, que é de 80 km/h")
    multa = (vel - 80) * 7
    print("Você deve pagar uma multa de R$ {:.2f}".format(float(multa)))
print("Tenha um bom dia! Dirija com segurança!")