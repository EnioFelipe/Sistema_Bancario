def depositar(saldo, extrato=None,/,):
    if extrato is None:
        extrato = {}

    valor=float(input("""               
            [1]Operação de depósito selecionada
              
            Digite a quantidade que deseja depositar:
                
            =>R$"""))
        
    if valor > 0:
            saldo += valor
            extrato.setdefault("Depósito", []).append(f"R$ {valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso!\nSaldo: R${saldo:.2f}")
    else:
            print("Depósito Inválido: Valor para depósito inválido.")

    return saldo, extrato


def sacar (*, saldo, extrato, contador_saque, limite_saque):
    
    valor = float(input("""
            [2]Operação de Saque selecionada
                            
            Digite a quantidade que deseja sacar:
                            
            =>R$"""))

    if valor <= 0:
        print("Saque inválido: Valor de saque inválido")

    elif valor > saldo:
        print("Saque inválido: Saldo insuficiente")

    elif contador_saque >= limite_saque:
        print("Saque inválido: Quantidade de saques diários atingida (3)")

    elif valor > 500:
        print("Saque inválido: O saque excedeu o limite de R$500,00")

    else:
        contador_saque += 1
        saldo -= valor
        extrato.setdefault("Saque", []).append(f"R$ {valor:.2f}")  

        print(f"""
            Saque de R${valor:.2f} realizado com sucesso!

            Saldo: R${saldo:.2f}
            """)
        
    return saldo, extrato, contador_saque


def apresentar_extrato (saldo,/,*,extrato):
    print("""
                           
            [3]Operação de Extrato selecionada
              
            """)
    
    print("====== EXTRATO ======")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        for operacao, detalhes in extrato.items():
            for detalhe in detalhes:
                print(f"{operacao}: {detalhe}")
    print(f"Saldo: R${saldo:.2f}")
    print("=====================")


def cadastrar_cliente(clientes):
    print("""
                           
            [4]Operação de Cadastrar Cliente selecionada
              
            """)
    
    cpf=int(input("Digite o CPF(Somente números):"))
    cliente=buscar_cliente(cpf,clientes)

    if cliente:
        print("ERRO: CPF já cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Cliente criado com sucesso! ===")


def buscar_cliente(cpf,clientes):
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            return cliente
    return 


def exibir_cliente(clientes):
    print("""
                           
            [5]Operação de Exibir Cliente selecionada
              
            """)
    cpf = int(input("Digite o CPF do usuário a ser exibido (somente número): "))
    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        print("\n=== Informações do Cliente ===")
        print(f"CPF: {cliente['cpf']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Data de Nascimento: {cliente['data_nascimento']}")
        print(f"Endereço: {cliente['endereco']}")
        print("=================================")
    else:
        print("ERRO: Cliente não encontrado!")


def criar_conta(contas,clientes,agencia,numero_conta):
    print("""
                           
            [6]Operação de Criar Conta selecionada
              
            """)
    cpf = int(input("Informe o CPF do cliente: "))
    cliente = buscar_cliente(cpf, clientes)

    if cliente:
        print("\n=== Conta criada com sucesso! ===")
        numero_conta = len(contas) + 1
        contas.append({"agencia": agencia, "numero_conta": numero_conta, "cliente": cliente})

    else:
        print("Cliente não encontrado! ")


def listar_contas(contas):
    print("""
                           
            [7]Operação de Listar contas selecionada
              
            """)
    
    for conta in contas:
        print (f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['cliente']['nome']}
        """)
              

def main():
    saldo = 0
    extrato = {}
    contador_saque = 0
    numero_conta=0
    clientes = []
    contas = []

    while True:

        op = input("""
                   OPÇÕES:

        [1]Depositar
        [2]Sacar
        [3]Extrato
        [4]Cadastrar Cliente
        [5]Exibir Cliente
        [6]Criar Conta
        [7]Listar Contas
        [0]Sair

        Escolha uma opção:""")

        if op=="1":
            saldo, extrato = depositar(saldo,extrato)
        
        elif op == "2":
            saldo, extrato, contador_saque = sacar(saldo=saldo, extrato=extrato, contador_saque=contador_saque, limite_saque=3)

        elif op=="3":
            apresentar_extrato(saldo, extrato=extrato)

        elif op=="4":
            cadastrar_cliente(clientes)
        
        elif op=="5":
            exibir_cliente(clientes)

        elif op =="6":
            criar_conta(contas, clientes, agencia="0001", numero_conta=numero_conta)
        
        elif op=="7":
            listar_contas(contas)

        elif op=="0":
            print("Saindo...")
            break

        else:
            print("Opção inválida, por favor selecione novamente a operação desejada.")

main()
