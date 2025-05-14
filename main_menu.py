from Product import Product
from inventoryfac import InventoryFacade
import os

def constroi_produto():
    produto = Product(
        name=input("Nome do produto: "),
        code=input("Código do produto: "),
        quantity=int(input("Quantidade: ")),
        category=input("Categoria: "),
        unit_cost=float(input("Valor unitário: "))
    )
    return produto

def fechar_enter():
    print("pressione enter para continuar")
    input()
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    facade = InventoryFacade()
    while True:
        print("""1 - Adicionar produto
2 - Atualizar produto
3 - Verificar quantidade de produtos em estoque
4 - Verificar valor do estoque atual
5 - Realizar uma compra
6 - historico de compras
7 - adicionar/remover funcionario
8 - mostrar os funcioanrios atuais
9 - fazer uma ordem de compra
10 - mostrar as ordens de compras
0 - Fechar programa""")
        choice = input("Proxima ação: ")
        os.system('cls' if os.name == 'nt' else 'clear')
        if choice == "0":
            print("Fechando o programa...")
            fechar_enter()
            break
        elif choice == "1":
            produto = constroi_produto()
            facade.adicionar_produto(produto)
            fechar_enter()
        elif choice == "2":
            codigo = input("Codigo do produto a ser atualizado: ")
            novo_produto = constroi_produto()
            facade.atualizar_produto(codigo, novo_produto)
            fechar_enter()
        elif choice == "3":
            facade.liste_produtos()
            fechar_enter()
        elif choice == "4":
            facade.valor_do_inventario()
            fechar_enter()
        elif choice == "5":
            codigo = input("Codigo do produto a ser comprado: ")
            quantidade = int(input("Quantidade a ser comprada: "))
            facade.comprar_produto(codigo, quantidade)
            fechar_enter()
        elif choice == "6":
            print("Historico de compras:\n")
            for compra in facade.historico:
                print(compra)
            fechar_enter()
        elif choice == "7":
            c = input("1 - adicionar fornecedor\n2- remover fornecedor\n")
            if c == "1":
                codigo = input("Codigo do fornecedor: ")
                name = input("Nome do fornecedor: ")
                facade.gerenciar_fornecedores(codigo = codigo, name = name)
            elif c == "2":
                codigo = input("Codigo do fornecedor: ")
                facade.gerenciar_fornecedores(codigo = codigo, remove = True)
            else:
                print("Opção inválida.")
            fechar_enter()
        elif choice == "8":
            print("Fornecedores:\n")
            for fornecedor in facade.fornecedores.values():
                print(f"Nome: {fornecedor.name}, Código: {fornecedor.code}")
            fechar_enter()
        elif choice == "9":
            codigo = input("Código do produto para repor: ")
            quantidade = int(input("Quantidade a ser reposta: "))
            facade.reestocar_produto(codigo, quantidade)
            fechar_enter()
        elif choice == "10":
            print("Ordens de compra:\n")
            for ordem in facade.historico_ordens:
                print(ordem)
            fechar_enter()
        else:
            print("Opção invalida.\n")
            fechar_enter()