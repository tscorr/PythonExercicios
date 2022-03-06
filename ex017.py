import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adajcente: '))
hip = math.hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))
