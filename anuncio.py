from abc import ABC, abstractmethod

class SubTipoInvalidoError(Exception):
    pass

class Anuncio(ABC):
    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        self._ancho = ancho if ancho > 0 else 1
        self._alto = alto if alto > 0 else 1
        self._url_archivo = url_archivo
        self._url_clic = url_clic
        self.sub_tipo = sub_tipo  # Utiliza el setter para validación

    @abstractmethod
    def comprimir_anuncio(self):
        pass

    @abstractmethod
    def redimensionar_anuncio(self):
        pass

    @staticmethod
    def mostrar_formatos():
        """
        Colabora con todas las subclases de Anuncio para mostrar los formatos y subtipos disponibles.
        """
        
        for cls in Anuncio.__subclasses__():
            print(f"FORMATO {cls.FORMATO}:")
            print("==========")
            for subtipo in cls.SUB_TIPOS:
                print(f"- {subtipo}")

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, value):
        self._ancho = value if value > 0 else 1

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, value):
        self._alto = value if value > 0 else 1

    @property
    def sub_tipo(self):
        return self._sub_tipo

    @sub_tipo.setter
    def sub_tipo(self, value):
        if value not in self.SUB_TIPOS:
            raise SubTipoInvalidoError(f"Subtipo {value} no válido para {self.FORMATO}")
        self._sub_tipo = value


class Video(Anuncio):
    FORMATO = "Video"
    SUB_TIPOS = ("instream", "outstream")

    def __init__(self, url_archivo: str, url_clic: str, sub_tipo: str, duracion: int):
        super().__init__(ancho=1, alto=1, url_archivo=url_archivo, url_clic=url_clic, sub_tipo=sub_tipo)
        self.duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    FORMATO = "Display"
    SUB_TIPOS = ("tradicional", "native")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    FORMATO = "Social"
    SUB_TIPOS = ("facebook", "linkedin")

    def __init__(self, ancho: int, alto: int, url_archivo: str, url_clic: str, sub_tipo: str):
        super().__init__(ancho, alto, url_archivo, url_clic, sub_tipo)

    def comprimir_anuncio(self):
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
