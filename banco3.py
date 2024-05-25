class Conta:
    def __init__(self,saldo,numero,agencia,cliente,historico):
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        self.cliente = cliente
        self.historico = historico
        saldo = float
        numero = int
        agencia = str
        cliente = Cliente
        historico = Historico
    def saldo(): 
        float
    def nova_conta(cliente,numero): 
        Conta
    def sacar(valor:float):
        bool
    def depositar(valor:float):
        bool


class Conta_corrente(Conta):
    def __init__(self,limite,limite_saques):
        self.limite = limite
        self.limite_saques = limite_saques
        limite = float
        limite_saques = int

class Cliente:
    def __init__(self,endereco,contas):
        self.endereco = endereco
        self.contas = contas 

class Pessoa_fisica(Cliente):
    def __init__(self,cpf,nome,data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Saque:
    def __init__(self,valor):
        self.valor = valor
        valor = float

class Deposito:
    def __init__(self,valor):
        self.valor = valor
        valor = float

class Transacao(Saque,Deposito):
    def __init__(self,valor):
        super().__init__(valor=valor)
    
    def Registrar_conta(conta:Conta):
        pass

class Historico():
    def adicionar_transacao(transacao):
        pass


