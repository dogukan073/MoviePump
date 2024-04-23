# from moviepy.editor import CompositeVideoClip, TextClip, VideoFileClip
# from moviepy.video.tools.subtitles import SubtitlesClip

from src.config import Config
from src.logger import Log


class VideoEditor:
    """
    Video Editor is responsable to add captions and format videos
    """

    def __init__(self) -> None:
        self.config = Config()
        self.log = Log()
        self.character_per_sec = 15

    def create_subtitles(self) -> str:
        pass

    def add_subtiles(self) -> bool:
        pass

    def create_narative(self) -> str:
        pass

    def add_narative(self) -> bool:
        pass

    def edit_video(self, video_name: str):
        self.log.logger.debug("Edit video start")

        self.log.logger.debug(f"{video_name} is used to create the video")
        # video = VideoFileClip("some.mp4")
        self.crop_video()
        # TODO generate srt file
        self.create_subtitles()
        self.add_subtiles()
        # TODO add sound
        self.create_narative()
        self.add_narative()

        # generator = lambda txt: TextClip(txt, font="Arial", fontsize=16, color="white")
        # subtitles = SubtitlesClip("somet.srt", generator)
        # video = VideoFileClip("some.mp4")
        # result = CompositeVideoClip([video, subtitles.set_pos(("center", "bottom"))])
        # result.write_videofile(
        #     "out.mp4",
        #     fps=video.fps,
        #     temp_audiofile="temp-audio.m4a",
        #     remove_temp=True,
        #     codec="libx264",
        #     audio_codec="aac",
        # )
