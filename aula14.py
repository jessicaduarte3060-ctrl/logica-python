soma = 0
contador = 0
pares = 0
impares = 0

numero = int(input("Digite um número: "))

while numero != 0:
    soma += numero
    contador += 1
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    numero = int(input("Digite outro número: "))

if contador > 0:
    media = soma / contador 

    print("Soma:", soma)
    print("Quantidade:", contador)
    print("Pares:", pares)
    print("Ímpares:", impares)
    print("Média:", media)
else:
    print("Nenhum número digitado.")