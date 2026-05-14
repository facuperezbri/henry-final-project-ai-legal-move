"""Tests para el parser de imágenes."""
import os
import sys
from dotenv import load_dotenv
from src.image_parser import parse_image

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)


load_dotenv()


def test_parse_image():
    """Test para el parser de imágenes."""
    image_path = "data/test_contracts/documento_1__original.jpg"

    if not os.path.exists(image_path):
        print(f"❌ Error: No se encontró la imagen en {image_path}")
        return

    print(f"🚀 Probando GPT-4o Vision con: {image_path}...")

    text = parse_image(image_path)
    print("\n--- ✅ RESULTADO ---")
    # Mostramos los primeros 500 caracteres
    print(text[:500] + "..." if len(text) > 500 else text)
    print("\n--- FIN DEL TEST ---")


if __name__ == "__main__":
    test_parse_image()
