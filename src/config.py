import os

from src.utils import SingletonMeta


class Config(metaclass=SingletonMeta):
    cwd = os.getcwd()
    debug = os.getenv("WORK_ENV") == "development"
    is_offline = os.getenv("IS_OFFLINE")
