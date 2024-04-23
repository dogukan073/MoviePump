""" """

import os
from typing import Optional

from pytube import YouTube

from src.config import Config
from src.db_manager.db_manager import DBManager
from src.exceptions import YoutubeIDException
from src.logger import Log
from src.utils import SingletonMeta

# TODO: File download to a remote file server ?


class YoutubeMan(metaclass=SingletonMeta):
    """
    Youtube Manager is responsible for youtube video downloads
    """

    def __init__(self, urls: Optional[list] = None, id: Optional[int] = 0) -> None:
        self.db_man = DBManager()
        self.log = Log()
        self.selected_url_id: int = id

        if not urls:
            urls = self.db_man.get_youtube_urls()

        self._youtube_urls: list = urls

    def download_video(self, url: Optional[str] = None) -> str:
        self.log.logger.debug("Start video download")
        if not url:
            if self.selected_url_id >= 0 and self.selected_url_id < len(self._youtube_urls):
                url = self._youtube_urls[self.selected_url_id]
            else:
                raise YoutubeIDException()

        yt = YouTube(url=url)
        self.log.logger.debug(f"Downloading: {yt.title} URL: {url}")
        output_path = os.path.join(Config.cwd, "downloads")
        name = ""
        try:
            yt.streams.first().download(filename=f"{yt.video_id}.mp4", output_path=output_path)
            self.log.logger.debug("Download Completed")
            name = f"{yt.video_id}.mp4"
            video = {
                "name": name,
                "update_date": "",
                "edit_completed": False,
                "edit_last_timestamp": "",
            }
            self.db_man.insert("downloads", "videos", video)
        except Exception as e:
            self.log.logger.debug(f"Download Failed, Reason: {str(e)}")

        return name

    def get_available_youtube_ids(self) -> list:
        return range(len(self._youtube_urls))

    def select_url(self, id: Optional[int]) -> None:
        self.selected_url_id = id
