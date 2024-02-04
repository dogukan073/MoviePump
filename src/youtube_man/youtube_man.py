""" """
import os
from typing import Optional

from pytube import YouTube

from src.config import Config
from src.db_manager.db_manager import DBManager
from src.exceptions import YoutubeIDException


class YoutubeMan:
    def __init__(self, urls: Optional[list] = None, id: Optional[int] = 0) -> None:
        """ """
        self.config = Config()
        self.db_man = DBManager()
        self.selected_url_id: int = id

        if not urls:
            urls = self.db_man.get_youtube_urls()

        self._youtube_urls: list = urls

    def download_video(self, url: Optional[str] = None):
        if not url:
            if self.selected_url_id >= 0 and self.selected_url_id < len(self._youtube_urls):
                url = self._youtube_urls[self.selected_url_id]
            else:
                raise YoutubeIDException()

        yt = YouTube(url=url)
        output_path = os.path.join(self.config.cwd, "downloads")
        yt.streams.first().download(filename="test.mp4", output_path=output_path)

    def get_available_youtube_ids(self):
        return range(len(self._youtube_urls))

    def select_url(self, id: Optional[int]):
        self.selected_url_id = id
