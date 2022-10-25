from datetime import datetime

from Entities.Cliente import Cliente
from Entities.Pedido import Pedido
from Entities.PedidoProduto import PedidoProduto
from Entities.Produto import Produto
from Repositories.ClienteRepository import ClienteRepository
from Repositories.PedidoRepository import PedidoRepository
from Repositories.ProdutoRepository import ProdutoRepository

customer1 = Cliente(1, "Jefté")
customer2 = Cliente(2, "João")
customer3 = Cliente(3, "Maria")
customer4 = Cliente(4, "José")

customer_repository = ClienteRepository()
customer_repository.adicionar_cliente(customer1)
customer_repository.adicionar_cliente(customer2)
customer_repository.adicionar_cliente(customer3)
customer_repository.adicionar_cliente(customer4)

product1 = Produto(1, "Milk", 8.78, 2)
product2 = Produto(2, "Bean", 11.00, 11)
product3 = Produto(3, "Rice", 10.23, 9)
product4 = Produto(4, "Noodle", 5.98, 6)

product_repository = ProdutoRepository()
product_repository.adicionar_produto(product1)
product_repository.adicionar_produto(product2)
product_repository.adicionar_produto(product3)
product_repository.adicionar_produto(product4)



pedido = Pedido(1, customer3, datetime.today)
order_product1 = PedidoProduto()
order_product2 = PedidoProduto()
print(order_product1.adicionar_produto(product2, 5))
print(order_product2.adicionar_produto(product3, 5))
pedido.adicionar_produto_pedido(order_product1)
pedido.adicionar_produto_pedido(order_product2)
pedido.atualizar_preco_total()

print("\n** Relatório de pedido **")
print(pedido)


print("\n** Relatório dos produtos **")
print(product_repository)
