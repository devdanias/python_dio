saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

menu = """
Escolha uma opção:
- (d) Depósito
- (s) Saque
- (e) Extrato
- (q) Sair
Opção: """

while True:
    opcao = input(menu)

    if opcao == "d":
        valor_deposito = float(input("Digite o valor do depósito: "))
        saldo += valor_deposito
        extrato += f"Depósito: + R${valor_deposito:.2f}\n"
        print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso.")

    elif opcao == "s":
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor do saque: "))
            if saldo - valor_saque >= -limite:
                saldo -= valor_saque
                extrato += f"Saque: - R${valor_saque:.2f}\n"
                numero_saques += 1
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso.")
            else:
                print("Saldo insuficiente para realizar o saque.")
        else:
            print("Limite de saques diários atingido.")

    elif opcao == "e":
        print(f"Saldo: R${saldo:.2f}\nExtrato:\n{extrato}")

    elif opcao == "q":
        print("Saindo do sistema.")
        break

    else:
        print("Operação inválida. Por favor, selecione novamente.")
