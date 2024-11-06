class Celular () :
    def __init__(self, marca , modelo, camara) :
        self.marca = marca
        self.modelo = modelo
        self.camara = camara
    
    def llamar(self) :
        print(f'estas haciendo una llamada desde un {self.modelo}')
         
    def cortar(self) :
        print(f'corto su llamada desde{self.modelo}')
        
celular1 = Celular("samsung" , "s23" , "48MP")
celular2 = Celular("apple" , "16pro" , "12MP")

celular2.llamar()

