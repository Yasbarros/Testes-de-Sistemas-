from Entities.Produto import Produto


class ProdutoRepository:

    def __init__(self) -> None:
        self.lista_produtos: list[Produto] = []

    def adicionar_produto(self, produto: Produto) -> None:
        self.lista_produtos.append(produto)

    def __str__(self) -> str:
        formatText = "{0:<10} {1:<20} {2:<20} {3:<20}\n"
        str_products = formatText.format("Id", "Descrição", "Preço Unitário", "Estoque")

        for item in self.lista_produtos:
            str_products += formatText.format(item.id, item.descricao, item.preco, item.estoque)

        return str_products
