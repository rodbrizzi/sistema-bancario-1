import os

# Função para limpar a tela do terminal
def limpar_tela():
    if os.name == 'posix':  # Unix/Linux/MacOS/BSD/etc
        _ = os.system('clear')
    elif os.name == 'nt':  # Windows
        _ = os.system('cls')

menu = """=============MENU BANCÁRIO=============

Escolha uma opção:
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair

=======================================
===> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    limpar_tela()
    opcao_escolhida = input(menu)

    if opcao_escolhida.lower() == "d":
        limpar_tela()
        valor = float(input("Informe o valor do depósito: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro na operação! O valor informado é inválido.")

    elif opcao_escolhida.lower() == "s":
        limpar_tela()
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Erro na operação! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Erro na operação! O valor do saque ultrapassa o limite.")
        elif excedeu_saques:
            print("Erro na operação! Número máximo de saques ultrapassado.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("Erro na operação! O valor informado é inválido.")

    elif opcao_escolhida.lower() == "e":
        limpar_tela()
        print("\n=============== EXTRATO ================")
        if not extrato:
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print("========================================")

    elif opcao_escolhida.lower() == "q":
        print("Programa finalizado. Até mais!")
        break

    else:
        limpar_tela()
        print("Operação inválida, por favor selecione corretamente a operação desejada.")

    input("\nPressione Enter para voltar ao menu...")
