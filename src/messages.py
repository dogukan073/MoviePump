import inspect
from typing import Optional

from src.db_manager.db_manager import DBManager
from src.utils import SingletonMeta


class Messages(metaclass=SingletonMeta):
    def __init__(self, lang: Optional[str] = "en") -> None:
        db_man = DBManager()
        self.messages = db_man.get_messages(lang=lang)

    @property
    def missing_youtube_id_exc(self) -> dict:
        return self.messages.get(inspect.currentframe().f_code.co_name)
