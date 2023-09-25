#REGRA DE DEPOSITO -> Não depositar valores negativos.
#REGRA DE SAQUE -> Permitir no maximo 3 saques diarios e não sacar sem saldo.
#REGRA DE EXTRATO -> Listar todos os depositos e todos os saques.

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor informado é inválido.")
    
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo:
            print("Operação falhou! Saldo insuficiente.")
            print(f"Saldo atual: R$ {saldo:.2f}\n")

        elif valor > limite:
            print("Operação falhou! Limite insuficiente.")
            print(f"Limite atual: R$ {limite:.2f}\n")

        elif numero_de_saques > limite_saques:
            print("Operação falhou! Limit de saques excedido.")
        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_de_saques += 1 

        else:
            print("Operação falhou! Valor informado é inválido.")

    elif opcao == "e":
        print("\n================================ EXTRATO ======================================")
        print("Não foi realizadas transações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================================================================")

    elif opcao == "q":
        break 

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada.")  
