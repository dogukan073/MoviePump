from src.db_manager.db import DB


class DBManager:
    def __init__(self):
        self.default_lang = "en"
        self.db = DB()

    def get_messages(self, lang: str = "en"):
        """
        Returns db containing message values of corresponding lang
        """
        if lang not in self.db.messages:
            lang = self.default_lang
        return self.db.messages.get(lang)

    def get_youtube_urls(self):
        return self.db.urls.get("urls")
