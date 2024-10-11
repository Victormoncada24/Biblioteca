import libro,miembro

class biblioteca():
    def __init__(self,id_biblioteca,nombre_biblioteca,direccion,id_libro,id_miembro):
        super().__init__(id_libro,id_miembro)
        self.id_biblioteca = id_biblioteca
        self.nombre_biblioteca = nombre_biblioteca
        self.direccion = direccion
    #Metodo vacio para luego implementar una busqueda mas exacta
    def buscar_libro():
        pass