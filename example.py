from video_scrapper.video_scrapper import VideoScrapper


def main():
    vs = VideoScrapper("links.txt")
    vs.download_videos()
    vs.download_audios()


if __name__ == "__main__":
    main()
