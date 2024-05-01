import yt_dlp


class PostProcessor(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        self.to_screen("Post processing stuff")
        return [], info
