s = float(input("Qual é o salário do funcionário? R$ "))
if s >= 1250:
    s*= 1.10
if s < 1250:
    s*= 1.15
print("Seu novo salário passará ser R${:.2f}".format(s))