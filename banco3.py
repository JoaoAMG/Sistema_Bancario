from datetime import datetime

class Transacao:
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data_hora = datetime.now()

    def registrar(self, conta):
        conta.saldo += self.valor
        conta.historico.adicionar_transacao(self)
        return True

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor
        self.data_hora = datetime.now()

    def registrar(self, conta):
        if conta.saldo >= self.valor:
            conta.saldo -= self.valor
            conta.historico.adicionar_transacao(self)
            return True
        return False

class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)

class Conta:
    def __init__(self, cliente, numero, agencia):
        self.saldo = 0.0
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = Historico()

    def sacar(self, valor):
        transacao = Saque(valor)
        return transacao.registrar(self)

    def depositar(self, valor):
        transacao = Deposito(valor)
        return transacao.registrar(self)

class ContaCorrente(Conta):
    def __init__(self, cliente, numero, agencia, limite, limite_saques):
        super().__init__(cliente, numero, agencia)
        self.limite = limite
        self.limite_saques = limite_saques

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        return transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, endereco, cpf, nome, data_nascimento):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


def menu():
    clientes = []

    while True:
        print("\n--- Menu do Sistema Bancário ---")
        print("1. Criar cliente")
        print("2. Criar conta")
        print("3. Realizar depósito")
        print("4. Realizar saque")
        print("5. Consultar saldo")
        print("6. Consultar histórico")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente(clientes)
        elif opcao == "2":
            criar_conta(clientes)
        elif opcao == "3":
            realizar_deposito(clientes)
        elif opcao == "4":
            realizar_saque(clientes)
        elif opcao == "5":
            consultar_saldo(clientes)
        elif opcao == "6":
            consultar_historico(clientes)
        elif opcao == "7":
            break
        else:
            print("Opção inválida!")

def criar_cliente(clientes):
    nome = input("Nome: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    data_nascimento = input("Data de Nascimento (dd/mm/yyyy): ")
    data_nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
    cliente = PessoaFisica(endereco, cpf, nome, data_nascimento)
    clientes.append(cliente)
    print("Cliente criado com sucesso!")

def criar_conta(clientes):
    cpf = input("CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if cliente:
        numero = input("Número da conta: ")
        agencia = input("Agência: ")
        conta = Conta(cliente, numero, agencia)
        cliente.adicionar_conta(conta)
        print("Conta criada com sucesso!")
    else:
        print("Cliente não encontrado!")

def realizar_deposito(clientes):
    cpf = input("CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if cliente:
        numero = input("Número da conta: ")
        conta = next((conta for conta in cliente.contas if conta.numero == numero), None)
        if conta:
            valor = float(input("Valor do depósito: "))
            if conta.depositar(valor):
                print("Depósito realizado com sucesso!")
            else:
                print("Falha no depósito!")
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

def realizar_saque(clientes):
    cpf = input("CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if cliente:
        numero = input("Número da conta: ")
        conta = next((conta for conta in cliente.contas if conta.numero == numero), None)
        if conta:
            valor = float(input("Valor do saque: "))
            if conta.sacar(valor):
                print("Saque realizado com sucesso!")
            else:
                print("Saldo insuficiente ou falha no saque!")
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

def consultar_saldo(clientes):
    cpf = input("CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if cliente:
        numero = input("Número da conta: ")
        conta = next((conta for conta in cliente.contas if conta.numero == numero), None)
        if conta:
            print(f"Saldo: R$ {conta.saldo:.2f}")
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

def consultar_historico(clientes):
    cpf = input("CPF do cliente: ")
    cliente = next((c for c in clientes if c.cpf == cpf), None)
    if cliente:
        numero = input("Número da conta: ")
        conta = next((conta for conta in cliente.contas if conta.numero == numero), None)
        if conta:
            print("Histórico de transações:")
            for transacao in conta.historico.transacoes:
                tipo = "Depósito" if isinstance(transacao, Deposito) else "Saque"
                print(f"{tipo} de R$ {transacao.valor:.2f} em {transacao.data_hora}")
        else:
            print("Conta não encontrada!")
    else:
        print("Cliente não encontrado!")

if __name__ == "__main__":
    menu()
