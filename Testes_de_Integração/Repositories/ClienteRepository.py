from Entities.Cliente import Cliente


class ClienteRepository:

    def __init__(self) -> None:
        self.lista_clientes: list[Cliente] = []

    def adicionar_cliente(self, cliente: Cliente) -> None:
        self.lista_clientes.append(cliente)

    def buscar_clientes(self) -> list[Cliente]:
        return self.lista_clientes
