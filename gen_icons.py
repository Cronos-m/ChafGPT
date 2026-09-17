# gen_icons.py
from PIL import Image
img = Image.open("icon.png").convert("RGBA")
for size in (192, 512):
    img.resize((size, size), Image.LANCZOS).save(f"icon-{size}.png")
    print(f"icon-{size}.png generado")
print("Listo. Sube icon.png, icon.ico, icon-192.png e icon-512.png al repo.")