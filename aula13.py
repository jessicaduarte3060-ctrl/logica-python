numero = int(input("Digite um número: "))

if numero == 0:
    print("Nenhum número digitado.")
else:
    maior = numero
    menor = numero

    while numero != 0:
        if numero > maior:
            maior = numero

        if numero < menor:
            menor = numero

        numero = int(input("Digite outro número: "))

    print("Maior número:", maior)
    print("Menor número:", menor)