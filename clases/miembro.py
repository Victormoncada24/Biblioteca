from rut_chile import rut_chile

class miembro():
    def __init__(self,id_miembro,nombre_miembro,telefono,correo,rut_usuario):
        self.id_miembro = id_miembro
        self.nombre_miembro = nombre_miembro
        self.telefono = telefono
        self.correo = correo
        self.rut_miembro = rut_miembro
    #Metodo validar rut haciendo llamada a la libreria rut_chile para verificarlo
    def validar_rut(self):
        return rut_chile.is_valid_rut(self.rut_miembro)    
