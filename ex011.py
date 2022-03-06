largura = float(input('Digite a largura da parede (em metros): '))
altura = float(input('Digite a altura da parede (em metros): '))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} e a área é de {}m²'.format(largura, altura, area))
print('A quantidade de tinta necessária para pintar esta parede é de {} litros'.format(area / 2))