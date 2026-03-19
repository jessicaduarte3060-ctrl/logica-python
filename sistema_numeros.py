while True:
    print("\n1 - Soma e média")
    print("2 - Pares e ímpares")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        soma = 0
        contador = 0

        numero = int(input("Digite um número: "))

        while numero != 0:
            soma += numero
            contador += 1
            numero = int(input("Digite outro número: "))

        if contador > 0:
            media = soma / contador
            print("Soma:", soma)
            print("Quantidade:", contador)
            print("Média:", media)
        else:
            print("Nenhum número digitado.")

    elif opcao == 2:
        pares = 0
        impares = 0

        numero = int(input("Digite um número: "))

        while numero != 0:
            if numero % 2 == 0:
                pares += 1
            else:
                impares += 1

            numero = int(input("Digite outro número: "))

        print("Pares:", pares)
        print("Ímpares:", impares)

    elif opcao == 0:
        print("Encerrando...")
        break

    else:
        print("Opção inválida.")