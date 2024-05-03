
saldo=0
saque=0
contador_saque=1
extrato=""

menu="""
    OPÇÕES:

    [1]Depositar
    [2]Sacar
    [3]Extrato
    [0]Sair

Escolha uma opção:"""

while True:

    op=(input(menu))
    print()

    if op=="1":

        deposito=float(input("""               
            [1]Operação de depósito selecionada
              
            Digite a quantidade que deseja depositar:
                
            =>R$"""))
        
        if deposito>0:

            saldo+=deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"

            print(f"""
                Depóstio de R${deposito:.2f} realizado com sucesso!

                Saldo: R${saldo:.2f}
                """)
            
        else:
            print("Depósito Inválido: Valor para depósito inválido.")
    
    elif op == "2":

        saque = float(input("""
            [2]Operação de Saque selecionada
                            
            Digite a quantidade que deseja sacar:
                            
            =>R$"""))

        if saque <= 0:
            print("Saque inválido: Valor de saque inválido")

        elif saque > saldo:
            print("Saque inválido: Saldo insuficiente")

        elif contador_saque > 3:
            print("Saque inválido: Quantidade de saques diários atingida (3)")

        elif saque > 500:
            print("Saque inválido: O saque excedeu o limite de R$500,00")

        else:
            contador_saque += 1
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"

            print(f"""
                Saque de R${saque:.2f} realizado com sucesso!

                Saldo: R${saldo:.2f}
                """)

    
    elif op=="3":

        print("""
                           
            [3]Operação de Extrato selecionada
              
            """)
        
        if extrato=="":
            print("\nNão foram realizadas movimentações.")

        else:
            print(f"======EXTRATO======\n{extrato}\nSaldo: R${saldo:.2f}\n=====================")

    elif op=="0":
        print("Saindo...")
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")