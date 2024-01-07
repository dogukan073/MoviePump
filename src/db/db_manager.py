class DBManager:
    def __init__(self):
        self.messages = {
            "en": {"missing_youtube_id_msg": "Please select an ID or provide a valid youtube url"}
        }

    def get_messages(self, lang: str = "en"):
        """
        Returns db containing message values of corresponding lang
        """
        if lang not in self.messages:
            lang = "en"
        return self.messages.get(lang)
