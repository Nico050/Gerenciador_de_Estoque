from account import Account

class AccountBuilder:
    def __init__(self):
        self.nome = None
        self.sobrenome = None
        self.cpf = None
        self.__senha = None

    def setar_nome(self, nome):
        self.nome = nome
        return self
    
    def setar_sobrenome(self, sobrenome):
        self.sobrenome = sobrenome
        return self
    
    def setar_cpf(self, cpf):
        self.cpf = cpf
        return self

    def setar_senha(self, senha):
        self.__senha = senha

    def pegar_senha(self):
        return self.__senha
    
    def build(self, db):
        if self.nome is None or self.nome.strip() == "":
            print("Seu nome está inválido")
            return False
        if self.sobrenome is None or self.sobrenome.strip() == "":
            print("Seu sobrenome está inválido")
            return False
        if (self.cpf is None or self.cpf.strip() == "" or
            not self.cpf.isdigit() or len(self.cpf) != 11):
            print("Seu CPF está inválido")
            return False
        if self.cpf in db["CPF"].astype(str).values:
            print("Já existe uma conta com este CPF.")
            return False
        if self.__senha is None or self.__senha.strip() == "" or self.__senha.isdigit():
            print("Sua senha está inválida")
            return False
        return True, Account(nome = self.nome, sobrenome = self.sobrenome, cpf = self.cpf, senha = self.pegar_senha())