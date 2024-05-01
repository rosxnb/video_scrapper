def max_duration_1min(info, *, incomplete):
    """
    Download videos with atmost duration of one minute.
    """
    duration = info.get("duration")
    if not duration or duration > 60:
        return f"[Filters] Video '{info.get("title")}' has duration {duration} seconds which exceeds max duration of 60 seconds \n\t unsucessful link: {info.get("webpage_url")}"
