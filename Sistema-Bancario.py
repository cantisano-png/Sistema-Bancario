menu = """

Olá! Informe a operação desejada!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opção = input(menu)

    if opção == "d":
        valor = float(input("\nInforme o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("\nOperação falhou! O valor informado para depósito é inválido.")

    elif opção == "s":
        valor = float(input("\nInforme o valor do saque: "))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\nOperação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("\nOperação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("\nOperação falhou! O número de máximo de saques diários foi excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("\nOperação falhou! O valor informado é inválido.")
            

    elif opção == "e":
        print("\n ==================EXTRATO==================\n")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=============================================")

    elif opção == "q":
        print("\nObrigado pela preferência, tenha um ótimo dia!")
        break

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")






