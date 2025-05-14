from Property import Property
class Product(Property):
    def __init__(self, name, unit_cost, quantity, code, category):
        super().__init__(name,code)
        self.unit_cost = unit_cost
        self.quantity = quantity
        self.category = category
    
    def __repr__(self):
        return (
            f"Nome: {self.name}\n"
            f"Código: {self.code}\n"
            f"Categoria: {self.category}\n"
            f"Valor unitário: {self.unit_cost}\n"
            f"Quantidade em estoque: {self.quantity}\n"
        )