from Entities.Pedido import Pedido


class PedidoRepository:
    def __init__(self) -> None:
        self.lista_pedidos: list[Pedido] = []

    def add_order(self, pedido: Pedido) -> None:
        self.lista_pedidos.append(pedido)
