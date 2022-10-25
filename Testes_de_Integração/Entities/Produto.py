class Produto:
    def __init__(self, id: int, descricao: str, preco: float, estoque: int) -> None:
        self.id = id
        self.descricao = descricao
        self.preco = preco
        self.estoque = estoque

    def verificar_estoque(self, quantidade) -> bool:
        if (self.estoque > quantidade):
            return True
        else:
            return False

    def baixar_estoque(self, quantidade) -> None:
        self.estoque -= quantidade
