# VideoScrapper

A wrapper around [yt-dlp](https://github.com/yt-dlp/yt-dlp).

- `VideoScrapper` class takes in a files that lists the links of videos to download each separated by newline.
- `_prepare_options` specifies the extension of `.mp4` for video files and `.wav` for audio files.


A demo of how `VideoScrapper` can be used is illustrated in file [example.py](./example.py).



# Running The Program

```sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python example.py
```


> Note: You may need to install ffmpeg binary. For MacOS refer below.

**Optional: FFMPEG binary install on MacOS**

Only do this if you are getting error related to ffmpeg.

```sh
brew install --formulae ffmpeg
```
