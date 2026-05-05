from app.utils.markdown_parser import load_markdown

class CVService:
    def get_cv_text(self):
        return load_markdown("app/data/cv.md")
