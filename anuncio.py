class Anuncio:
    """
    Clase base para representar un anuncio publicitario.

    Atributos:
        alto (int): Altura del anuncio, debe ser mayor a 0.
        ancho (int): Ancho del anuncio, debe ser mayor a 0.
        sub_tipo (str): Subtipo de anuncio permitido.

    Métodos:
        mostrar_formatos(): Método estático que muestra los formatos y subtipos disponibles.
    """

    def __init__(self, alto, ancho, sub_tipo):
        """
        Inicializa un anuncio con los valores de alto, ancho y subtipo.

        Parámetros:
            alto (int): Altura del anuncio.
            ancho (int): Ancho del anuncio.
            sub_tipo (str): Subtipo del anuncio.

        Excepciones:
            SubTipoInvalidoException: Si el subtipo no es válido para el tipo de anuncio.
        """
        self.alto = alto if alto > 0 else 1
        self.ancho = ancho if ancho > 0 else 1
        if sub_tipo in self.SUB_TIPOS:
            self.sub_tipo = sub_tipo
        else:
            raise Exception("SubTipoInvalidoException")

    @staticmethod
    def mostrar_formatos():
        """
        Muestra los formatos disponibles para los anuncios.

        Retorna:
            None
        """
        print("Formatos disponibles:")
        for subtipo in Anuncio.SUB_TIPOS:
            print(f"- {subtipo}")


class Video(Anuncio):
    """
    Clase que representa un anuncio de tipo Video.

    Atributos:
        duracion (int): Duración del video en segundos, debe ser mayor a 0.

    Métodos:
        comprimir_anuncio(): Muestra un mensaje que indica que la compresión no está implementada.
        redimensionar_anuncio(): Muestra un mensaje que indica que el recorte no está implementado.
    """

    def __init__(self, duracion):
        """
        Inicializa un anuncio de tipo Video.

        Parámetros:
            duracion (int): Duración del video.

        Excepciones:
            Ninguna, pero si la duración es menor o igual a 0, se asigna un valor de 5 segundos.
        """
        super().__init__(1, 1, "Corto")
        self.duracion = duracion if duracion > 0 else 5

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión de video no está implementada."""
        print("COMPRESIÓN DE VIDEO NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el recorte de video no está implementado."""
        print("RECORTE DE VIDEO NO IMPLEMENTADO AÚN")


class Display(Anuncio):
    """
    Clase que representa un anuncio de tipo Display.

    Métodos:
        comprimir_anuncio(): Muestra un mensaje que indica que la compresión no está implementada.
        redimensionar_anuncio(): Muestra un mensaje que indica que el redimensionamiento no está implementado.
    """

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión de anuncios Display no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DISPLAY NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el redimensionamiento de anuncios Display no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DISPLAY NO IMPLEMENTADO AÚN")


class Social(Anuncio):
    """
    Clase que representa un anuncio de tipo Social.

    Métodos:
        comprimir_anuncio(): Muestra un mensaje que indica que la compresión no está implementada.
        redimensionar_anuncio(): Muestra un mensaje que indica que el redimensionamiento no está implementado.
    """

    def comprimir_anuncio(self):
        """Muestra un mensaje indicando que la compresión de anuncios de redes sociales no está implementada."""
        print("COMPRESIÓN DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADA AÚN")

    def redimensionar_anuncio(self):
        """Muestra un mensaje indicando que el redimensionamiento de anuncios de redes sociales no está implementado."""
        print("REDIMENSIONAMIENTO DE ANUNCIOS DE REDES SOCIALES NO IMPLEMENTADO AÚN")
