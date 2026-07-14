# TODO: to extract the audio from given url

from typing import Any, cast
import yt_dlp


def extract_audio(url: str, output_dir: str = ".") -> None:
    opts: dict[str, Any] = {
        "format": "bestaudio/best",
        "outtmpl": f"{output_dir}/%(title)s.%(ext)s",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
            }
        ],
    }
    with yt_dlp.YoutubeDL(cast(Any, opts)) as ydl:
        result = ydl.download([url])
        if result != 0:
            raise RuntimeError(f"yt-dlp failed with exit code {result}")
