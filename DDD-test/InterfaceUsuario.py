from DestinoRepository import DestinoRepository

class InterfaceUsuario:
    def __init__(self, destino_repository):
        self.destino_repository =  destino_repository


    def solicitar_input_usuario(self):
        input_usuario = int(input("Digite o DDD para descobrir o destino: "))
        return input_usuario        
    
    def exibir_destinos(self):
        return self.destino_repository.buscar_destinos()

    def saida_usuario(self, ddd):
        return self.destino_repository.obter_destino_pelo_ddd(ddd)
    

    