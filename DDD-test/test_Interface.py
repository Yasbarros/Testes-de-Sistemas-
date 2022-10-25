from Destino import Destino
from DestinoRepository import DestinoRepository
from InterfaceUsuario import InterfaceUsuario

def test_saida_usuario():
    # arrange
    destino1 = Destino(61, "Brasilia")
    destino_repository = DestinoRepository()
    destino_repository.adicionar_destino(destino1)
    interface_usuario = InterfaceUsuario(destino_repository)

    # act
    destino = interface_usuario.saida_usuario(61)
   

    # assert
    assert destino == "Brasilia"
