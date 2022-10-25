from datetime import datetime

from Entities.Cliente import Cliente
from Entities.PedidoProduto import PedidoProduto


class Pedido:
    def __init__(self, id: int, cliente: Cliente, data: datetime) -> None:
        self.id = id
        self.cliente = cliente
        self.data = data
        self.pedido_produto: list[PedidoProduto] = []
        self.valor_total: float = 0

    def adicionar_produto_pedido(self, pedido_produto: PedidoProduto) -> None:
        if (hasattr(pedido_produto, "produto")):
            self.pedido_produto.append(pedido_produto)

    def atualizar_preco_total(self) -> None:
        for produto in self.pedido_produto:
            self.valor_total += produto.valor_item

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20} {4:<20}\n"
        str_products = f"Cliente: {self.cliente.nome} Valor total do pedido: {self.valor_total}\n"

        str_products += formatText.format(
            "Id", "Descrição", "Preço", "Quantidade", "Preço Total Item")

        for order_product in self.pedido_produto:
            str_products += formatText.format(order_product.produto.id,
                                              order_product.produto.descricao, order_product.produto.preco, order_product.quantidade, order_product.valor_item)

        return str_products
