from Entities.Produto import Produto


class PedidoProduto:
    def __init__(self) -> None:
        self.valor_item: float
        self.quantidade: int
        self.produto: Produto

    def adicionar_produto(self, product: Produto, quantidade: int) -> str:
        if (not product.verificar_estoque(quantidade)):
            return f"Produto sem '{product.descricao}' estoque."

        self.processar_pedido(product, quantidade)
        return "Produto adicionado com sucesso!"

    def processar_pedido(self, produto: Produto, quantidade: int) -> None:
        self.produto = produto
        produto.baixar_estoque(quantidade)
        self.valor_item = produto.preco * quantidade
        self.quantidade = quantidade
