"""
Agent para contextualizar el contrato y la adenda.
"""
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()


class ContextualizationAgent:
    """
    Agent para contextualizar el contrato y la adenda.
    """

    def __init__(self):
        # Usamos temperature 0 para que el análisis sea determinista y profesional
        self.llm = ChatOpenAI(model="gpt-4o", temperature=0)

    def get_context_map(self, contract_text: str, amendment_text: str) -> str:
        """
        Obtiene el mapa contextual entre el contrato original y la adenda.
        """
        system_prompt = """
        Eres un Analista Legal Senior especializado en auditoría de contratos.
        Tu tarea es recibir el texto de un CONTRATO ORIGINAL y una ADENDA (enmienda).

        Debes producir un ' facilite Mapa Contextual' la extracción de cambios posterior.

        Tu output debe incluir:
        1. Resumen del propósito del contrato original.
        2. Identificación de las cláusulas del contrato original que están siendo mencionadas en la adenda.
        3. Estructura comparativa: (Ejemplo: 'La sección 4 de la adenda modifica el anexo B del contrato').

        No extraigas los cambios todavía, solo establece el puente entre ambos documentos.
        """

        prompt = ChatPromptTemplate.from_messages([
            ("system", system_prompt),
            ("user", "CONTRATO ORIGINAL:\n{contract}\n\nADENDA:\n{amendment}")
        ])

        # Unimos el prompt con el modelo (chain)
        chain = prompt | self.llm

        response = chain.invoke({
            "contract": contract_text,
            "amendment": amendment_text
        })

        return response.content
