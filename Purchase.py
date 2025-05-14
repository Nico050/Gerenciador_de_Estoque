class Purchase:
    def __init__(self, _unit_cost, _quantity, _code , _cost):
        self._unit_cost = _unit_cost
        self._cost = _cost
        self._quantity = _quantity
        self._code = _code
    
    def __repr__(self):
        return (
            f"Código: {self._code}\n"
            f"Valor unitário: {self._unit_cost}\n"
            f"Quantidade comprada: {self._quantity}\n"
            f"Custo total: {self._cost}\n"
        ) 