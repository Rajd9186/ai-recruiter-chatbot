from utils.markdown_parser import load_markdown


class BaseAgent:
    """Simple base agent class placeholder."""
    pass


class CVService:
    def get_cv_text(self):
        return load_markdown("data/cv.md")
