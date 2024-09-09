from campania import campania
from anuncio import Video
from error import LargoExcedidoException, SubTipoInvalidoException
from datetime import date

# Crear campaña inicial con un anuncio de tipo Video
anuncios_data = [
    {
        "tipo": "Video",
        "anuncio_data": {
            "duracion": 10
        }
    }
]

# Crear la campaña
try:
    campaña = campania("Campaña inicial", date(2024, 1, 1), date(2024, 12, 31))

    for anuncio_data in anuncios_data:
        tipo = anuncio_data["tipo"]
        data = anuncio_data["anuncio_data"]
        campaña.agregar_anuncio(tipo, data)

    # Solicitar nuevo nombre de la campaña
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    campaña.nombre = nuevo_nombre

    # Solicitar nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo del anuncio: ")
    if campaña.anuncios:
        campaña.anuncios[0].sub_tipo = nuevo_subtipo

except LargoExcedidoException as e:
    with open('error.log', 'a') as f:
        f.write(f"Error: {e}\n")
    print(f"Error: {e}")

except SubTipoInvalidoException as e:
    with open('error.log', 'a') as f:
        f.write(f"Error: {e}\n")
    print(f"Error: {e}")

print(campaña)
