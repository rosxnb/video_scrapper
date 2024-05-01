import os
from yt_dlp import YoutubeDL
from video_scrapper import (
    filters,
    options,
    post_processor,
    logger,
    exceptions
)


class VideoScrapper:
    def __init__(
        self,
        links_file_path=None,
        output_path="archives"
    ):
        self._read_file(links_file_path)
        self._prepare_options(output_path)

    def download_videos(self):
        with YoutubeDL(self.video_options) as ydl:
            ydl.add_post_processor(post_processor.PostProcessor(), when="pre_process")
            ydl.download(self.links)

    def download_audios(self):
        with YoutubeDL(self.audio_options) as ydl:
            ydl.add_post_processor(post_processor.PostProcessor(), when="pre_process")
            ydl.download(self.links)

    def _read_file(self, file_path):
        try:
            with open(file_path, "r") as f:
                self.links = f.read().splitlines()
        except FileNotFoundError:
            exceptions.VideoScrapperException(f"Invalid {file_path = }")

    def _prepare_options(self, output_path):
        self.video_options = {
            "match_filter": filters.max_duration_1min,
            "format": options.format_selector,
            "logger": logger.Logger(),
            "progress_hooks": [
                options.progress_hook
            ],
            "paths": {
                "home": output_path,
            },
        }
        
        self.audio_options = {
            "match_filter": filters.max_duration_1min,
            "format": "wav/bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
            }],
            "logger": logger.Logger(),
            "progress_hooks": [
                options.progress_hook
            ],
            "paths": {
                "home": output_path,
            },
        }

    def __len__(self):
        return len(self.links)
