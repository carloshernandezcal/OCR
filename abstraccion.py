class Auto ():
    def __init__(self):
        self._estado = "encendido" 
        
    def encender(self):
        self._estado = "encendido"
        print("el auito esta encendido")
        
    def conducir(self):
          if self._estado == "apagado" :
               self.encender()
          print("conduciendo auto")

mi_auto = Auto()
mi_auto.conducir()