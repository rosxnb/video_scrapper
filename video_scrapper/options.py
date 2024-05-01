def progress_hook(table):
    if table["status"] == "finished":
        print(f"SAVED: {table["info_dict"]["title"]}")


def format_selector(ctx):
    # formats are alread sorted worst to best
    formats = ctx.get("formats")[::-1]

    # acodec="none" means there is no audio
    best_video = next(f for f in formats
                      if f['vcodec'] != "none" and f['acodec'] == "none" and f['ext'] == "mp4")

    # find compatible audio extension
    audio_ext = {
        "mp4": "m4a",
        "webm": "webm"
    }[best_video['ext']]

    # vcodec="none" means there is no video
    best_audio = next(f for f in formats if (
        f["acodec"] != "none" and f["vcodec"] == "none" and f["ext"] == audio_ext
    ))

    yield {
        "format_id": f"{best_video["format_id"]}+{best_audio["format_id"]}",
        "ext": best_video["ext"],
        "requested_formats": [best_video, best_audio],
        "protocol": f"{best_video["protocol"]}+{best_audio["protocol"]}"
    }
