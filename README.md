# Nonmbre Proyecto: Prueba Python

## Descripción del proyecto

Este proyecto es una aplicación orientada a objetos que permite gestionar campañas publicitarias y sus anuncios asociados. Utiliza el principio de herencia para manejar diferentes tipos de anuncios (Video, Display, Social) y emplea un sistema de manejo de errores personalizados para validar atributos como el tamaño del anuncio y el subtipo de cada uno.

El proyecto incluye:

-La creación de campañas publicitarias con diferentes anuncios.
-Validaciones de formato y tipo de anuncio.
-Manejo de errores personalizados.
-Un archivo **demo.py** para ejecutar y probar las funcionalidades

## Archivos del Proyecto

1-**campania.py**: Contiene la clase Campaña, que gestiona una colección de anuncios.
2-**anuncio.py**: Contiene las clases Anuncio, Video, Display, Social, que representan los distintos tipos de anuncios.
3-**errores.py**: Define las excepciones personalizadas como **LargoExcedidoException** y **SubTipoInvalidoException**.
4-**demo.py**: Archivo que simula una serie de interacciones predefinidas para probar el correcto funcionamiento del sistema.
5-**error.log**: Archivo de registro donde se almacenan errores capturados durante la ejecución del programa (si se genera).
6-**README.md**: Archivo con la descripción del proyecto, los archivos y los requisitos.

## Requisitos

Python 3.x: El proyecto está escrito en Python, por lo que necesitas tener instalada la versión 3.x de Python.
Librerías estándar de Python: El proyecto utiliza bibliotecas como datetime, os (opcional, dependiendo de cómo implementes el manejo de errores).
Sistema de Archivos: El proyecto puede generar archivos de registro de errores y ejecutará el demo. Asegúrate de tener permisos de escritura en el directorio donde se ejecute.

## Instalación del Proyecto

Clona el repositorio:

```bash
git clone https://github.com/KarenLimari/Pruebapython.git
```

## Instrucciones para Ejecutar el Proyecto

```bash
cd demo.py
```

## Autor

Arlenis Gonzalez - Karen Limari - Ambar Zambrano

## Licencia

Este proyecto está bajo la Licencia MIT - consulta el archivo LICENSE.md para más detalles.
