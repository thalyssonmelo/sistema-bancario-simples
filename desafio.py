menu = """

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

def depositar(valor:float):
    global extrato
    global saldo
    if valor > 0:
        extrato += f"Depósito: R$ {valor:.2f}\n"
        saldo += valor
    else :
        print("Operação falhou! O valor informado é inválido.\n")    

def sacar(valor:float):
    global extrato
    global saldo
    global LIMITE_SAQUES
    global limite
    if LIMITE_SAQUES > 0:  
        if valor <= limite:
            if valor <= saldo:
                extrato += f"Saque R$ {valor:.2f}\n"
                saldo -= valor
                LIMITE_SAQUES -= 1
            else:
                print("Operação falhou! Você não tem saldo suficiente.")
        else:
            print("Operação falhou! O valor do saque excede o limite.")            
    else:
        print("Operação falhou! Número máximo de saques excedidos.") 

def mostrar_extrato():
    global extrato
    global saldo
    if extrato != "":
        string_extrato = " EXTRATO "
        print(string_extrato.center(42,"="))
        print(f"{extrato}")
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=" * 42)
    else:
        print("Não foram realizadas movimentações.")    

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Depósito")
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)

    elif opcao == "s":
        print("Saque")
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)

    elif opcao == "e":
        mostrar_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")          