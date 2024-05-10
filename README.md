# Sistema Bancário 🏦

Este é um projeto desenvolvido como parte do curso de Formação em Python da plataforma DIO.

## Funcionalidades

O sistema apresenta um menu com as seguintes funcionalidades:

1. **Depósito:** Permite realizar operações de depósito em uma conta bancária.
2. **Saque:** Permite realizar operações de saque em uma conta bancária, com restrições específicas.
3. **Extrato:** Exibe o extrato da conta bancária, mostrando todas as movimentações realizadas.
4. **Cadastrar Cliente:** Permite cadastrar novos clientes no sistema.
5. **Exibir Cliente:** Exibe informações detalhadas de um cliente cadastrado.
6. **Criar Conta:** Permite a criação de novas contas associadas a clientes existentes.
7. **Listar Contas:** Exibe uma lista de todas as contas cadastradas no sistema.

## Restrições e Observações

### Depósito

- O valor a ser depositado deve ser maior do que zero.

### Saque

- O valor do saque deve ser maior do que zero e menor ou igual ao saldo disponível na conta.
- Existe um limite máximo de R$500,00 para cada saque.
- Cada cliente pode realizar no máximo três saques por dia.

### Extrato

- Se não houver movimentações, será exibida uma mensagem informando que não foram realizadas operações.
- Caso contrário, será exibido o extrato completo da conta.

### Cadastrar Cliente

- O CPF do cliente deve ser único no sistema. Não é permitido cadastrar dois clientes com o mesmo CPF.
- Todos os campos de informações do cliente (nome, data de nascimento, endereço) devem ser preenchidos de forma válida.
- Caso um CPF já esteja cadastrado no sistema, não será permitido cadastrar o mesmo cliente novamente com o mesmo CPF.

### Exibir Cliente

- É necessário informar o CPF válido do cliente para exibir suas informações.
- O cliente deve estar cadastrado no sistema para que suas informações possam ser exibidas.
- Se o cliente não for encontrado com o CPF informado, será exibida uma mensagem informando que o cliente não foi encontrado no sistema.

### Criar Conta

- O cliente para o qual a conta será criada deve estar previamente cadastrado no sistema.
- É necessário informar o CPF do cliente para associar a nova conta ao cliente correspondente.
- O número da agência e da conta podem ser gerados automaticamente ou serem fornecidos pelo usuário.
- Caso o CPF informado não corresponda a nenhum cliente cadastrado, a operação de criar conta não será concluída e será exibida uma mensagem informando que o cliente não foi encontrado no sistema.

### Listar Contas

- Não existem restrições específicas para a operação de listar contas.

## Como Executar

Para executar o sistema, basta rodar o arquivo principal `main.py`.
