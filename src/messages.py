import inspect

from src.db.db_manager import DBManager


class Messages:
    def __init__(self, lang="en") -> None:
        db_man = DBManager()
        self.messages = db_man.get_messages(lang=lang)

    @property
    def missing_youtube_id_msg(self):
        return self.messages.get(inspect.currentframe().f_code.co_name)
