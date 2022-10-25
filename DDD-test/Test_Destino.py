from DestinoRepository import DestinoRepository
from Destino import Destino

def test_adicionar_destino():
    #arrange 
    Destino1 = Destino(61, "Brasilia")
    destino_repository = DestinoRepository()

    #act 
    destino_repository.adicionar_destino(Destino1)

    #assert 
    assert len(destino_repository.lista_destino) == 1


def test_checar_se_destino_existe():
    #arrange
    Destino1 = Destino(61,"Brasilia")
    Destino2 = Destino(71,"Salvador")
    destino_repository = DestinoRepository()

    #act
    destino_repository.adicionar_destino(Destino1)

    
    #assert
    assert destino_repository.checa_se_destino_existe(61) == True

    assert destino_repository.checa_se_destino_existe(71) == False 



def test_obter_destino_pelo_ddd():
    #arrange 
    Destino1 = Destino(61, "Brasilia")
    destino_repository = DestinoRepository()

    #act 
    destino_repository.adicionar_destino(Destino1)

    

    #assert 
    assert destino_repository.obter_destino_pelo_ddd(61) == "Brasilia"

    assert destino_repository.obter_destino_pelo_ddd(20) == "Destino não encontrado"
    


