import datetime

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = f""
transacoes = 0
LIMITE_TRANSACOES = 10
data = datetime.datetime.now().strftime("%A %d/%m/%Y")
hora = datetime.datetime.now().strftime("%H:%M")


def depositar(saldo, valor, extrato, transacoes, data, hora):
    if valor <= 0:
        print("Valor inválido para depósito.")
    elif transacoes >= LIMITE_TRANSACOES:
        print("Número máximo de transacoes atingido!")
    elif valor > 0:
        saldo += valor
        extrato += f"{data} {hora} - Depósito: R$ {valor:.2f}\n"
        transacoes += 1
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato, transacoes, data, hora

def sacar(saldo, valor, limite, extrato, transacoes, data, hora):
    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("Valor acima do limite!")
    elif transacoes >= LIMITE_TRANSACOES:
        print("Número máximo de transacoes atingido!")
    elif valor > 0:
        saldo -= valor
        extrato += f"{data} {hora} - Saque: R$ {valor:.2f}\n"
        transacoes += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para saque.")
    return saldo, extrato, transacoes, data, hora

def exibir_extrato(saldo, extrato, data, hora):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu).strip().lower()
    if opcao == "1":
        valor_input = input("Valor para depósito: R$ ")
        try:
            valor = float(valor_input)
        except ValueError:
            print("Valor inválido para depósito.")
            continue
        saldo, extrato, transacoes, data, hora = depositar(saldo, valor, extrato, transacoes, data, hora)
    elif opcao == "2":
        valor_input = input("Valor para saque: R$ ")
        try:
            valor = float(valor_input)
        except ValueError:
            print("Valor inválido para saque.")
            continue
        saldo, extrato, transacoes, data, hora = sacar(saldo, valor, limite, extrato, transacoes, data, hora)
    elif opcao == "3":
        exibir_extrato(saldo, extrato, data, hora)
    elif opcao == "4":
        print("Saindo da conta.")
        break
    else:
        print("Opção inválida! Tente novamente.")