# models/data_models.py
from dataclasses import dataclass, field
from typing import List, Optional, Dict


@dataclass
class TranscriptItem:
    """Representa um segmento de transcrição de vídeo."""
    text: str
    start: float
    duration: float


@dataclass
class TranscriptInfo:
    """Informações sobre uma transcrição disponível."""
    language_code: str
    language: str
    is_generated: bool
    is_translatable: bool


@dataclass
class Video:
    """Representa um vídeo do YouTube com sua transcrição."""
    id: str
    title: str
    transcript: Optional[List[TranscriptItem]] = None
    available_transcripts: List[TranscriptInfo] = field(default_factory=list)
    language_used: Optional[str] = None  # Armazena qual idioma foi usado na transcrição final


@dataclass
class Playlist:
    """Representa uma playlist do YouTube com múltiplos vídeos."""
    id: str
    title: str
    videos: List[Video]

    @property
    def video_count(self) -> int:
        """Retorna o número total de vídeos na playlist."""
        return len(self.videos)

    @property
    def videos_with_transcript(self) -> List[Video]:
        """Retorna apenas os vídeos que possuem transcrição."""
        return [video for video in self.videos if video.transcript is not None]

    @property
    def transcript_count(self) -> int:
        """Retorna o número de vídeos com transcrição."""
        return len(self.videos_with_transcript)

    @property
    def languages_used(self) -> Dict[str, int]:
        """Retorna um dicionário com a contagem de cada idioma usado nas transcrições."""
        languages = {}
        for video in self.videos:
            if video.language_used:
                if video.language_used in languages:
                    languages[video.language_used] += 1
                else:
                    languages[video.language_used] = 1
        return languages