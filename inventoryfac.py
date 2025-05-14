from Product import Product
from Purchase import Purchase
from Suplier import Suplier

class InventoryFacade:
    def __init__(self):
        self.inventario = {}
        self.fornecedores = {}
        self.historico = []
        self.historico_ordens = []

    def adicionar_produto(self, produto):
        if produto.code in self.inventario:
            print("Produto já existe no inventário.\n")
            return False
        self.inventario[produto.code] = produto
        self._verificar_quantidade_produto(produto)
        return True
    
    def atualizar_produto(self, codigo, novo_produto):
        if codigo not in self.inventario:
            print("Produto não encontrado no inventário.\n")
            return False
        del self.inventario[codigo]
        self.inventario[novo_produto.code] = novo_produto
        self._verificar_quantidade_produto(novo_produto)
        return True
    
    def liste_produtos(self):
        for codigo, produto in self.inventario.items():
            print(f"Código: {codigo}, Nome: {produto.name}, Quantidade: {produto.quantity}\n")

    def valor_do_inventario(self):
        total = sum(p.unit_cost * p.quantity for p in self.inventario.values())
        print(f"Valor total do inventario: R$ {total:.2f}\n")

    def comprar_produto(self, codigo, quantidade):
        produto = self.inventario.get(codigo)
        if not produto:
            print("Produto não encontrado no inventário.\n")
            return False
        if produto.quantity < quantidade:
            print(f"Quantidade insuficiente, Estoque atual: {produto.quantity}\n")
            return False
        produto.quantity -= quantidade
        self.historico.append(self._faz_compra(produto, quantidade))
        self._verificar_quantidade_produto(produto)
        return True
    
    def reestocar_produto(self, codigo, quantidade):
        produto = self.inventario.get(codigo)
        if not produto:
            print("Produto não encontrado no inventário.\n")
            return False
        produto.quantity += quantidade
        self.historico_ordens.append(self._faz_compra(produto, quantidade))
        return True
    
    def gerenciar_fornecedores(self, codigo, name = None, remove = False):
        if remove:
            if codigo in self.fornecedores:
                del self.fornecedores[codigo]
                print(f"Fornecedor {codigo} removido com sucesso!\n")
                return True
            print("Fornecedor não encontrado.\n")
            return False
        else:
            self.fornecedores[codigo] = Suplier(name, codigo)
            return True
        
    def _verificar_quantidade_produto(self, produto):
        if produto.quantity <= 3:
            print(f"Produto de código: {produto.code} com estoque baixo ({produto.quantity} unidade(s))\n")
    
    def _faz_compra(self, produto, quantidade):
        return Purchase(
            _code = produto.code,
            _unit_cost = produto.unit_cost,
            _quantity = quantidade,
            _cost = produto.unit_cost * quantidade
        )