from utils.markdown_parser import load_markdown

CV_TEXT = load_markdown(r"C:\Users\rajde\source\repos\AgentJob\app\data\cv.md")

class RetrievalService:
    def get_context(self, query: str):
        return CV_TEXT
