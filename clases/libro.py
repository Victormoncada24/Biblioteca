import categoria

#Aqui tenemos abstraccion ya que buscamos los atributos necesarios para la creacion de esta clase
class libro(categoria):
    def __init__(self,id_libro,nombre_libro,autor,fecha_publicacion,estado,id_categoria_libro):
        super().__init__(id_categoria_libro)
        self.id_libro = id_libro
        self.nombre_libro = nombre_libro
        self.autor = autor
        self.fecha_publicacion = fecha_publicacion
        self.estado = estado
    