from anuncio import Video, Display, Social
from datetime import date

class LargoExcedidoError(Exception):
    pass

class Campaña:
    def __init__(self, nombre: str, fecha_inicio: date, fecha_termino: date, anuncios_data: list):
        if len(nombre) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres")
        self._nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.fecha_termino = fecha_termino
        self._anuncios = self._crear_anuncios(anuncios_data)

    def _crear_anuncios(self, anuncios_data):
        """
        Este método privado crea los anuncios basados en los datos proporcionados
        y los almacena como parte de la composición de la clase Campaña.
        """
        anuncios = []
        for anuncio_data in anuncios_data:
            tipo = anuncio_data.get("tipo")
            if tipo == "video":
                anuncios.append(Video(**anuncio_data["params"]))
            elif tipo == "display":
                anuncios.append(Display(**anuncio_data["params"]))
            elif tipo == "social":
                anuncios.append(Social(**anuncio_data["params"]))
        return anuncios

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if len(value) > 250:
            raise LargoExcedidoError("El nombre de la campaña excede los 250 caracteres")
        self._nombre = value

    @property
    def anuncios(self):
        return self._anuncios

    def __str__(self):
        video_count = sum(isinstance(anuncio, Video) for anuncio in self._anuncios)
        display_count = sum(isinstance(anuncio, Display) for anuncio in self._anuncios)
        social_count = sum(isinstance(anuncio, Social) for anuncio in self._anuncios)

        return (f"Nombre de la campaña: {self._nombre}\n"
                f"Anuncios: {video_count} Video, {display_count} Display, {social_count} Social")
