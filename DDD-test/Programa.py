from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

destino_repository = DestinoRepository()
 

destino1 = Destino(61, "Brasilia")
destino2 = Destino(71, "Salvador")
destino3 = Destino(11, "São Paulo")
destino4 = Destino(21, "Rio de Janeiro")
destino5 = Destino(32, "Juiz de Fora")
destino6 = Destino(19, "Campinas")
destino7 = Destino(27, "Vitoria")
destino8 = Destino(31, "Belo Horizonte")

destino_repository.adicionar_destino(destino1)
destino_repository.adicionar_destino(destino2)
destino_repository.adicionar_destino(destino3)
destino_repository.adicionar_destino(destino4)
destino_repository.adicionar_destino(destino5)
destino_repository.adicionar_destino(destino6)
destino_repository.adicionar_destino(destino7)
destino_repository.adicionar_destino(destino8)


interface_usuario = InterfaceUsuario(destino_repository)
print(interface_usuario.exibir_destinos())
ddd = interface_usuario.solicitar_input_usuario()

print(interface_usuario.saida_usuario(ddd))
