"""Parser de imágenes de documentos legales."""
import base64
import os
from src.config import get_llm

client = get_llm()


def encode_image(image_path: str) -> str:
    """Convierte una imagen local a un string en base64."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"La imagen {image_path} no existe.")

    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def parse_image(image_path: str) -> str:
    """Envía la imagen al LLM para que la analice y devuelva el texto."""
    base64_image = encode_image(image_path)

    prompt = """
    Extrae todo el texto contenido en esta imagen de documento legal.
    Mantén la estructura de parráfos, numeración de clausulas y encabezados. (IMPORTANTE)
    No resumas, no interpretes, solo transcribe de forma literal.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        temperature=0.0,
    )
    return response.choices[0].message.content or ""
