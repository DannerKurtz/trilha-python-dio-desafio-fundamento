menu = """


[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair


=>"""

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("\nInforme um valor para depósito!\n=>"))

        if valor > 0:
            saldo += valor
            extrato += f"Deposito: R$ {valor:.2f}\n"
        else:
            print("Valor inválido")
    
    elif opcao == "2":
        valor = float(input("\nInforme um valor para saque!\n=>"))

        excedeu_saldo = saldo < valor
        excedeu_limite = limite < valor
        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1
        
    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("Sistema finalizado!")
        break

    else:
        ("Opção não é valida")
