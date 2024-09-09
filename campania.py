from datetime import date
from anuncio import Video, Display, Social, SubTipoInvalidoError


# Excepción para error de largo de anuncios
class LargoExcedidoError(Exception):
    pass


class campania:
    """
    Clase que representa una campaña publicitaria, que agrupa distintos anuncios.

    Attributos
    ----------
    nombre : str
        Nombre de la campaña publicitaria.
    fecha_inicio : date
        Fecha de inicio de la campaña.
    fecha_termino : date
        Fecha de término de la campaña.
    anuncios : list
        Lista que contiene los anuncios asociados a la campaña.

    Métodos
    -------
    agregar_anuncio(anuncio_data, tipo):
        Agrega un anuncio a la campaña según el tipo especificado.
    __str__():
        Retorna una representación en cadena de la campaña con el número de anuncios por tipo.
    """

    # constructor, acá están los atributos de la clase campania
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date):
        """
        Inicializa la clase Campaña con los atributos nombre, fecha de inicio y término.

        Parámetros
        ----------
        nombre : str
            El nombre de la campaña publicitaria.
        fecha_inicio : date
            La fecha de inicio de la campaña.
        fecha_termino : date
            La fecha de término de la campaña.
        """
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self.anuncios = []

    # Propiedades y setters para decha_inicio y fecha_termino
    @property
    def fecha_inicio(self):
        return self.fecha_inicio

    @fecha_inicio.setter
    def fecha_inicio(self, value):
        # Validamos que la fecha_inicio (value)sea del tipo 'date'
        if not isinstance(
            value, date
        ):  # insintance() función para verificar si un objeto es de un tipo o clase específica.Devuelve True si el objeto pertenece y False en caso contrario
            raise ValueError("fecha_inicio debe ser de tipo 'date'.")
        self._fecha_inicio = value

    @property
    def fecha_termino(self):
        return self.fecha_termino

    @fecha_termino.setter
    def fecha_termino(self, value):
        # Validamos que la fecha_termino(value) sea del tipo 'date'
        if not isinstance(
            value, date
        ):  # insintance() función para verificar si un objeto es de un tipo o clase específica.Devuelve True si el objeto pertenece y False en caso contrario
            raise ValueError("fecha_termino debe ser de tipo 'date'.")
        self._fecha_termino = value

    def agregar_anuncio(sefl, tipo: str, anuncio_data: dict):
        """
        Agrega un anuncio a la campaña según el tipo especificado.

        Parámetros
        ----------
        anuncio_data : dict
            Diccionario con los datos del anuncio (como ancho, alto, url, etc.).
        tipo : str
            Tipo de anuncio que puede ser "Video", "Display" o "Social".

        Raises
        ------
        SubTipoInvalidoError
            Si el subtipo del anuncio no es válido según el tipo.
        """
        try:
            if tipo == "Video":
                # Crea una instancia de Video y la agrega a la lista de anuncios.
                self.anuncios.append(Video(**anuncio_data))
            elif tipo == "Display":
                # Crea una instancia de Display y la agrega a la lista de anuncios.
                self.anuncios.append(Display(**anuncio_data))
            elif tipo == "Social":
                # Crea una instancia de Social y la agrega a la lista de anuncios.
                self.anuncios.append(Social(**anuncio_data))
            else:
                # Si el tipo de anuncio no es válido, lanza un error.
                raise ValueError(f"Tipo de anuncio'{tipo} no es válido.")
        except SubTipoInvalidoError as e:
            print(f"Error al agregar anuncio {e}")
