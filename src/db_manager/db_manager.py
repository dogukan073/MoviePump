import traceback
from typing import Optional

from src.db_manager.db import DB
from src.utils import SingletonMeta


class DBManager(metaclass=SingletonMeta):
    def __init__(self):
        self.default_lang = "en"
        self.db = DB()

    def get_messages(self, lang: Optional[str] = "en"):
        """
        Returns db containing message values of corresponding lang
        """
        messages = self.db.get("messages")
        if lang not in messages:
            lang = self.default_lang
        return messages.get("result").get(lang)

    def get_youtube_urls(self) -> list:
        urls = self.db.get("urls", "urls")
        return urls.get("result")

    def get_video(self, video_id: int) -> list:
        video = self.db.get("downloads", "videos", _id=video_id)
        return video.get("result")

    def insert(self, collection_name: str, key: str, value: str):
        result = False
        try:
            self.db.insert(collection_name, key, value)
            result = True
        except Exception:
            traceback.print_exc()

        return result
