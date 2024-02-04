import json
import os

from src.config import Config


class DB:
    def __init__(self) -> None:
        self.config = Config()
        self.db_loc = os.path.join(self.config.cwd, "src", "db_manager", "db")

    @property
    def messages(self):
        messages_loc = os.path.join(self.db_loc, "messages.json")
        with open(messages_loc, "r") as f:
            m = json.load(f)
        return m

    @property
    def urls(self):
        urls_loc = os.path.join(self.db_loc, "urls.json")
        with open(urls_loc, "r") as f:
            u = json.load(f)
        return u
