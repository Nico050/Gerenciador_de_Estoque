from Property import Property
class Suplier(Property):
    def __init__(self,name,code):
        super().__init__(name,code)
    
    def __repr__(self):
        return(f"Nome: {self.name}" f" | Código: {self.code}\n")
