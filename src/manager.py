from src.youtube_man.youtube_man import YoutubeMan


class Manager:
    def __init__(self) -> None:
        self.youtube_man = YoutubeMan()

    def run(self):
        self.youtube_man.download_video()
