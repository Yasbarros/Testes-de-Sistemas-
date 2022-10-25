from Destino import Destino

class DestinoRepository:

    def __init__(self):
        self.lista_destino = []

    def adicionar_destino(self, destino):
        self.lista_destino.append(destino)

    def checa_se_destino_existe(self, ddd):
        for destino in self.lista_destino:
            if(destino.ddd == ddd):
                return True 
            
        return False

    def obter_destino_pelo_ddd(self, ddd):
        for destino in self.lista_destino:
            if(destino.ddd == ddd):
                return destino.destino
        return 'Destino não encontrado'
    
    def buscar_destinos(self):
        formatText = "{0:<10} {1:<20} \n"
        menu = formatText.format("DDD", "Destino")

        for destino in self.lista_destino:
            menu += formatText.format(destino.ddd, destino.destino)

        return menu

    