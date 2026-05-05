
from agents.base_agent import BaseAgent
from services.retrieval_service import RetrievalService
from utils.prompt_builder import build_prompt
from core.config import llm

class RecruiterAgent(BaseAgent):
    def __init__(self):
        self.retrieval = RetrievalService()

    def handle(self, query: str):
        context = self.retrieval.get_context(query)
        prompt = build_prompt(context, query)
        return llm(prompt)