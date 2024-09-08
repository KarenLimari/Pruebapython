from datetime import date

class LargoExcedidoError(Exception):
    pass

class campania:
    #constructor, acá están los atributos de la clase campania
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date):
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.anuncios = []

    #Propiedades y setters para decha_inicio y fecha_termino
    @property
    def fecha_inicio(self):
        return self.fecha_inicio
    
    @fecha_inicio.setter
    def fecha_inicio(self, value):
        #Validamos que la fecha_inicio (value)sea del tipo 'date'
        if not isinstance(value, date): #insintance() función para verificar si un objeto es de un tipo o clase específica.Devuelve True si el objeto pertenece y False en caso contrario
            raise ValueError("fecha_inicio debe ser de tipo 'date'.")
        self._fecha_inicio = value

    @property
    def fecha_termino(self):
        return self.fecha_termino
    
    @fecha_termino.setter
    def fecha_termino(self, value):
        #Validamos que la fecha_termino(value) sea del tipo 'date'
        if not isinstance(value, date): #insintance() función para verificar si un objeto es de un tipo o clase específica.Devuelve True si el objeto pertenece y False en caso contrario
            raise ValueError("fecha_termino debe ser de tipo 'date'.")
        self._fecha_termino = value