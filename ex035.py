print("-=-" * 20)
print("Analisador de triângulos")
print("-=-" * 20)
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
if a < b + c and b < a + c and c < a + b:
    print("Os segmentos acima PODEM FORMAR TRIÃNGULO")
else:
    print("Os segmentos acima NÃO PODEM FORMAR TRIÂNGULO")