from src.config import Config
from src.db_manager.db_manager import DBManager
from src.logger import Log
from src.video_editor import VideoEditor
from src.youtube_manager import YoutubeMan


class Manager:
    def __init__(self) -> None:
        self.youtube_man = YoutubeMan()
        self.video_editor = VideoEditor()
        self.log = Log()
        self.db_manager = DBManager()

        self._should_download = not Config.is_offline
        self._active_video_id = 0

    def check_video(self) -> str:
        # TODO
        video_name = None

        video = self.db_manager.get_video(video_id=self._active_video_id)

        if video and video.get("edit_completed"):
            video_name = video.get("name")

        return video_name

    def run(self) -> None:
        self.log.logger.debug("Starting")
        # task_should_run = True
        # while task_should_run:
        if self._should_download:
            downloaded = self.youtube_man.download_video()
            if not downloaded:
                self.log.logger.error("Video Download Error")

        video_name = self.check_video()

        # start video editor
        self._should_download = self.video_editor.edit_video(video_name=video_name)

        self.log.logger.debug("Done")
