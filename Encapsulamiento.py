# class Miclase :
#     def __init__(self) -> None:
#         self.__atributo_privado = "valor"
        
# objeto = Miclase()
# print(objeto._atributo_privado)

class Persona ():
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
    
    def get_nombre(self):
        return self.nombre

    def set_nombre(self,new_nombre):
        self.nombre = new_nombre

andres = Persona( "andres" , 37 )


nombre = andres.get_nombre()
print(nombre)    
                 
andres.set_nombre("pepe")                 

nombre = andres.get_nombre()
print(nombre) 