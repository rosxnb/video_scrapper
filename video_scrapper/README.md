## Potential things to try out and keep in considerations

**Did you Know:**

- YouTube videos has "categories".


## Yt-dlp things:

**All info about a video**


To extract information to a file:
```python
def info_extractor():
    url = "https://www.youtube.com/watch?v=MQbmEIG0evI"

    with yt_dlp.YoutubeDL() as ydl:
        info = ydl.extract_info(url, download=False)
        print(json.dumps(ydl.sanitize_info(info)))
```


We can use that information to filter out videos or audios:
```python
def extract_audio():
    def audio_duration_filter(info, *, incomplete):
        duration = info.get("duration")
        if duration and duration > 120:
            return f"Duration too long, should be under 2 minutes. \n {info.get("title") = }"

    def print_category(info, *, incomplete):
        return f"{info.get("categories") = }"

    ydl_opts = {
        "format": "wav/bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
        }],
        "match_filter": print_category,
    }

    url = "https://www.youtube.com/watch?v=MQbmEIG0evI"
    url = "https://www.youtube.com/watch?v=U5lapdSkEWY"
    url = "https://www.youtube.com/watch?v=7-dL6a5_B3I&t=13s"
    url = "https://www.youtube.com/watch?v=7wZUvZJgD4A"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        _ = ydl.download(url)
```
