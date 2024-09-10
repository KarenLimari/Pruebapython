from campaña import Campaña, LargoExcedidoError
from anuncio import SubTipoInvalidoError
from datetime import date

# Crear campaña inicial con un anuncio de tipo Video
anuncios_data = [
    {
        "tipo": "video",
        "params": {
            "url_archivo": "http://video.mp4",
            "url_clic": "https://www.youtube.com/watch?v=an7krXQW4aU",
            "sub_tipo": "instream",
            "duracion": 10
        }
    }
]

campaña = Campaña("Campaña inicial", date(2024, 1, 1), date(2024, 12, 31), anuncios_data)

try:
    # Solicitar nuevo nombre de la campaña
    nuevo_nombre = input("Ingrese el nuevo nombre de la campaña: ")
    campaña.nombre = nuevo_nombre

    # Solicitar nuevo subtipo para el anuncio
    nuevo_subtipo = input("Ingrese el nuevo subtipo del anuncio: ")
    campaña.anuncios[0].sub_tipo = nuevo_subtipo

except LargoExcedidoError as e:
    with open('error.log', 'a') as f:
        f.write(f"Error: {e}\n")
    print(f"Error: {e}")

except SubTipoInvalidoError as e:
    with open('error.log', 'a') as f:
        f.write(f"Error: {e}\n")
    print(f"Error: {e}")

print(campaña)
