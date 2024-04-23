import logging
import logging.config

from src.config import Config
from src.utils import SingletonMeta


class Log(metaclass=SingletonMeta):

    def __init__(self) -> None:
        logging.config.dictConfig(
            {
                "version": 1,
                "disable_existing_loggers": True,
            }
        )
        logging.basicConfig(
            level=logging.DEBUG if Config.debug else logging.WARNING,
            format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        )
        self.logger_prop = logging.getLogger(__name__)

    @property
    def logger(self):
        return self.logger_prop
