"""
Agente para extraer los cambios del contrato y la adenda.
"""

from langchain_core.prompts import ChatPromptTemplate
from src.models import ContractChangeOutput
from src.config import get_llm


class ExtractionAgent:
    """
    Agente para extraer los cambios del contrato y la adenda.
    """

    def __init__(self):
        self.llm = get_llm().with_structured_output(
            ContractChangeOutput)

        def extract_changes(self, contract_text: str, amendment_text: str, context_map: str) -> ContractChangeOutput:
            system_prompt = """
            Eres un Auditor Legal Senior especializado en auditoría de contratos. Tu trabajo es identificar los cambios realizados en el contrato original y la adenda.

            Para hcaerlo vas a recibir un mapa contextual ya identificó qué áreas analizar.

            Reglas estrictas:
            1. Si una sección no recibió cambios, no la incluyas en el output.
            2. Clasifica los cambios detectados en categorías comerciales o legales claras para el campo 'topics_touched'.
            3. En el campo 'summary_of_the_change' sé explícito: qué decía el contrato original y qué dice ahora la adenda.
            """

            prompt = ChatPromptTemplate.from_messages([
                ("system", system_prompt),
                ("user",
                 "CONTRATO ORIGINAL:\n{contract}\n\nADENDA:\n{amendment}\n\nMAPA CONTEXTUAL:\n{context}")
            ])

            chain = prompt | self.llm

            response = chain.invoke({
                "contract": contract_text,
                "amendment": amendment_text,
                "context": context_map

            })

            return response
