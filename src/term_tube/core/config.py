# TODO: :  Default config for package
from configparser import ConfigParser
from pathlib import Path

CONFIG_FILE = Path(__file__).parent / "config.ini"

_parser = ConfigParser(interpolation=None)
_ = _parser.read(CONFIG_FILE)

MUSIC_DIR = Path(_parser.get("paths", "music_dir", fallback="~/Music")).expanduser()
AUDIO_FORMAT = _parser.get("audio", "format", fallback="mp3")
AUDIO_QUALITY = _parser.get("audio", "quality", fallback="192")
EMBED_METADATA = _parser.getboolean("audio", "embed_metadata", fallback=True)
EMBED_THUMBNAIL = _parser.getboolean("audio", "embed_thumbnail", fallback=False)
