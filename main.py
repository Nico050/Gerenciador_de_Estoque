from abc import ABC, abstractmethod
from account import *
from main_menu import *
import os

atualcpf = None

class Menus(ABC):
    @abstractmethod
    def start(self):
        pass

class Login_Menu(Menus):
    global atualcpf
    def start(self):
        db = encontre_usuario()
        print("Bem vindo ao sistema de gerenciamento de estoque!")
        print("Para iniciarmos, faça seu login ou registre sua conta!")
        print("1. Login\n2. Registrar\n3. Sair")
        choice = int(input("Escolha uma opção: "))
        if choice == 1:
            efet, atualcpf = login(db)
            if efet == False:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.start()
            fechar_enter()
        elif choice == 2:
            db, atualcpf = registrar(db)
            if atualcpf == None:
                os.system('cls' if os.name == 'nt' else 'clear')
                self.start()
            fechar_enter()
        elif choice == 3:
            print("Saindo...")
            fechar_enter()
            exit()


class Main_Menu(Menus):

    def start(self):
        main()

login_menu = Login_Menu()
main_menu = Main_Menu()
login_menu.start()
main_menu.start()
