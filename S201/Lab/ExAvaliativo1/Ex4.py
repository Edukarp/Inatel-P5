class Televisao:

    def __init__(self, modelo):
        self.modelo = modelo
        self.canal = "none"
        self.volume = 0

    def aumentar_volume(self,valor):
        self.volume += valor

    def diminuir_volume(self,valor):
        if(valor > self.volume):
            self.volume = 0
        else:
            self.volume -= valor

    def trocar_canal(self, canal):
        self.canal = canal

    def mostra_info(self):
        print("Modelo: ", self.modelo, " Canal: ", self.canal, " Volume: ", self.volume)


class SmartTV(Televisao):
    def __init__(self, modelo):
        super().__init__(modelo)
        self.canal = "none"
        self.volume = 0
        self.intenet = False

    def conectar_internet(self):
        self.intenet = True

    def mostra_info(self):
        print("Modelo: ", self.modelo, " Canal: ", self.canal, " Volume: ", self.volume, " Conexao: ", self.intenet)



televisao1 = Televisao("LG")
televisao1.mostra_info() #Antes
televisao1.aumentar_volume(70)
televisao1.diminuir_volume(27)
televisao1.trocar_canal("Canal 1")
televisao1.mostra_info() #Depois

televisao2 = SmartTV("Sony")
televisao2.mostra_info() #Antes
televisao2.aumentar_volume(80)
televisao2.diminuir_volume(10)
televisao2.trocar_canal("Canal 2")
televisao2.conectar_internet() #Depois
televisao2.mostra_info()
