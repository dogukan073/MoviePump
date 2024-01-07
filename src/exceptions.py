from src.messages import Messages


class BaseException(Exception):
    pass


class YoutubeIDException(BaseException):
    def __init__(self, message=Messages().missing_youtube_id_msg) -> None:
        super().__init__(message)
