"""
Configuración de la aplicación.
"""
from langchain_openai import ChatOpenAI


def get_llm(model: str = "gpt-4o", temperature: float = 0) -> ChatOpenAI:
    """Centraliza la configuración del modelo de LLM."""
    return ChatOpenAI(model=model, temperature=temperature)
