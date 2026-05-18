"""
Pipeline de análisis legal autónomo.
"""
import os
from langfuse.decorators import observe, langfuse_context
from dotenv import load_dotenv
from src.image_parser import parse_image
from src.agents.contextualization_agent import ContextualizationAgent
from src.agents.extraction_agent import ExtractionAgent

load_dotenv()


@observe()
def run_contract_pipeline(original_path: str, amendment_path: str):
    """
    Pipeline de análisis legal autónomo.
    """
    # Langfuse setup
    langfuse_context.update_current_trace(
        name="Contract-Comparison-Pipeline",
        public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    )

    print("🎬 Empezando el pipeline de análisis legal autónomo...")

    print("🎨 Parsea el contrato original...")
    original_text = parse_image(original_path)

    print("🎨 Parsea la adenda...")
    amendment_text = parse_image(amendment_path)

    print("🎨 Contextualiza el contrato y la adenda...")
    contextualization_agent = ContextualizationAgent()
    context_map = contextualization_agent.get_context_map(
        original_text, amendment_text)

    print("🔍 Extrae los cambios estructurados...")
    extraction_agent = ExtractionAgent()

    # This returns a validated ContractChangeOutput Pydantic object
    validated_output = extraction_agent.extract_changes(
        contract_text=original_text,
        amendment_text=amendment_text,
        context_map=context_map
    )

    print("✨ Pipeline completado con éxito!")
    return validated_output
