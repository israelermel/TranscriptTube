from dataclasses import dataclass
from typing import List, Optional

@dataclass
class TranscriptItem:
    text: str
    start: float
    duration: float

@dataclass
class Video:
    id: str
    title: str
    transcript: Optional[List[TranscriptItem]] = None

@dataclass
class Playlist:
    id: str
    title: str
    videos: List[Video]