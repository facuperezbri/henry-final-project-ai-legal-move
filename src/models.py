"""Modelo validado con pydantic para la salida del ExtractionAgent."""

from typing import List
from pydantic import BaseModel, Field


class ContractChangeOutput(BaseModel):
    """Este modelo define la estructura final que el ExtractionAgent debe entregar."""
    sections_changed: List[str] = Field(
        description="""
        Identificadores exactos de las cláusulas o secciones modificadas (ej: 'Cláusula Quinta', 'Anexo B').
        """)
    topics_touched: List[str] = Field(
        description="""
        Categorías legales afectadas por los cambios (ej: 'Responsabilidad Civil', 'Plazos de entrega', 'Confidencialidad').
        """)
    summary_of_the_change: str = Field(
        description="""
        Un resumen ejecutivo y técnico que explique qué decía el original y cómo lo modificó la adenda.
        """)
