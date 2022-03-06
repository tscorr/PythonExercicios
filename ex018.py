from math import radians, sin, cos, tan
ang = float(input('Digite um ângulo qualquer: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O seno de {} é {:.2f}'.format(ang, sen))
print('O cosseno de {} é {:.2f}'.format(ang, cos))
print('A tangente de {} é {:.2f}'.format(ang, tan))
