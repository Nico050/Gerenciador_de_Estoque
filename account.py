import pandas as pd
import os

def encontre_usuario():
    if os.path.exists("usuarios.csv"):
        df = pd.read_csv("usuarios.csv", dtype={"CPF": str})
        return df
    else:
        df = pd.DataFrame(columns= ["Nome", "Sobrenome", "CPF", "Senha"])
        return df

class Account:
    def __init__(self, nome, sobrenome, cpf, senha):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.__senha = senha

    def por_senha(self, senha):
        return self.__senha == senha
    def pegar_senha(self):
        return self.__senha

from accountbuilder import AccountBuilder

def registrar(db):
    print("Registrar conta!")
    ab = AccountBuilder()
    ab.setar_nome(input("Digite seu nome: ").strip())
    ab.setar_sobrenome(input("Digite seu sobrenome: ").strip())
    ab.setar_cpf(input("Digite seu CPF: ").strip())
    ab.setar_senha(input("Digite sua senha: ").strip())
    print(ab.nome, ab.sobrenome, ab.cpf)
    signal, account = ab.build(db)
    if not signal:
        return db, None
        
    tempDB = pd.DataFrame({
        "Nome": [account.nome],
        "Sobrenome": [account.sobrenome],
        "CPF": [account.cpf],
        "Senha": [account.pegar_senha()]
    })
    db = pd.concat([db, tempDB], ignore_index=True)
    db.to_csv("usuarios.csv", index=False)

    print("Conta criada com sucesso!")
    return db, account.cpf
    
def login(db):
    print("Login na conta!")
    id = input("Digite seu CPF: ").strip()
    s = input("Digite sua senha: ").strip()
    cpf = db[db["CPF"].astype(str) == id]
    if not cpf.empty and cpf.iloc[0]["Senha"] == s:
        print("Login bem sucedido!")
        return True, id
    else:
        print("Login falhou! Senha ou CPF incorretos.")
        return False
