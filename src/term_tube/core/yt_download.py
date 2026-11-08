# TODO: Check a simple url request to extract audio using ytdlp
from pathlib import Path

import yt_dlp
from term_tube.config import (
    AUDIO_FORMAT,
    AUDIO_QUALITY,
    EMBED_METADATA,
    EMBED_THUMBNAIL,
    MUSIC_DIR,
)


def download_audio(url: str, output_dir: Path = MUSIC_DIR) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    postprocessors = [
        {
            "key": "FFmpegExtractAudio",  # --extract-audio
            "preferredcodec": AUDIO_FORMAT,  # --audio-format
            "preferredquality": AUDIO_QUALITY,  # --audio-quality
        }
    ]
    if EMBED_METADATA:
        postprocessors.append({"key": "FFmpegMetadata"})  # --embed-metadata
    if EMBED_THUMBNAIL:
        postprocessors.append({"key": "EmbedThumbnail"})  # --embed-thumbnail

    options = {
        "format": "bestaudio/best",
        "outtmpl": str(output_dir / "%(title)s.%(ext)s"),
        "writethumbnail": EMBED_THUMBNAIL,
        "postprocessors": postprocessors,
    }

    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])
