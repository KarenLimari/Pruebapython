﻿# Nombre Proyecto: Prueba Python

## Descripción del proyecto

Este proyecto es una aplicación orientada a objetos que permite gestionar campañas publicitarias y sus anuncios asociados. Utiliza el principio de herencia para manejar diferentes tipos de anuncios (Video, Display, Social) y emplea un sistema de manejo de errores personalizados para validar atributos como el tamaño del anuncio y el subtipo de cada uno.

El proyecto incluye:

-La creación de campañas publicitarias con diferentes anuncios.
-Validaciones de formato y tipo de anuncio.
-Manejo de errores personalizados.
-Un archivo **demo.py** para ejecutar y probar las funcionalidades

## Archivos del Proyecto

## Archivos

El proyecto consta de los siguientes archivos:

1. **`campaña.py`**:

   - Contiene la implementación de la clase `Campaña`.
   - Esta clase permite gestionar una campaña publicitaria que puede contener anuncios de tipo `Video`, `Display` y `Social`.
   - También maneja excepciones específicas como `LargoExcedidoError` y `SubTipoInvalidoException` en casos de errores.
   - Propiedades de validación para las fechas de inicio y término de la campaña.

2. **`anuncio.py`**:

   - Implementa las clases base para los anuncios: `Anuncio`, `Video`, `Display` y `Social`.
   - Define comportamientos específicos para cada tipo de anuncio, como la compresión y el redimensionamiento.
   - Incluye validación del subtipo de anuncios mediante el uso de excepciones.
   - Relacionado directamente con `Campania`, ya que los anuncios se agregan a una campaña.

3. **`error.py`**:

   - Contiene excepciones personalizadas como `LargoExcedidoException` y `SubTipoInvalidoException`.
   - Estas excepciones se usan en las clases `Campania` y `Anuncio` para manejar errores específicos, como cuando el nombre de una campaña excede los 250 caracteres o cuando se asigna un subtipo no válido de anuncio.

4. **`demo.py`**:

   - Este archivo contiene el código para ejecutar y probar el programa.
   - Muestra ejemplos de cómo crear campañas y anuncios, agregarlos, y manejar errores mediante excepciones.
   - Sirve como archivo principal para ver la interacción entre todas las clases y módulos.

5. **`error.log`**:
   - **Descripción**: Este archivo registra los errores y excepciones que se producen durante la ejecución del programa. Es útil para depurar problemas y rastrear fallos.

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
