import sys
from PIL import Image

def crear_archivo_prueba():
    """
    Genera una imagen de 200x200 pixeles de color negro 
    con un patron de cuadrante para validar la creacion de archivos.
    """
    try:
        # Crear el lienzo
        imagen = Image.new('RGB', (200, 200), color='black')
        
        # Pintar cuadrantes de diferentes colores
        for x in range(100):
            for y in range(100):
                imagen.putpixel((x, y), (255, 0, 0))     # Rojo
                imagen.putpixel((x + 100, y), (0, 255, 0)) # Verde
                imagen.putpixel((x, y + 100), (0, 0, 255)) # Azul
                imagen.putpixel((x + 100, y + 100), (255, 255, 255)) # Blanco

        # Guardar el resultado en el disco
        ruta_salida = 'artefacto_magico.png'
        imagen.save(ruta_salida)
        print(f"Ejecucion exitosa. El archivo '{ruta_salida}' ha sido materializado en el directorio actual.")
        
    except Exception as e:
        print(f"Error durante la ejecucion del conjuro: {e}", file=sys.stderr)

if __name__ == "__main__":
    crear_archivo_prueba()