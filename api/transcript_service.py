from youtube_transcript_api import YouTubeTranscriptApi, _errors
from typing import List, Optional
from models.data_models import TranscriptItem, Video, Playlist


class TranscriptService:
    @staticmethod
    def get_transcript(video_id: str, languages: List[str] = ['pt', 'en']) -> Optional[List[dict]]:
        """Obtém a transcrição do vídeo usando a API de transcrição do YouTube."""
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            return transcript
        except _errors.NoTranscriptFound:
            print(f"Nenhuma transcrição encontrada para o vídeo ID: {video_id}")
            return None
        except Exception as e:
            print(f"Erro ao obter transcrição: {str(e)}")
            return None

    @staticmethod
    def add_transcript_to_video(video: Video) -> Video:
        """Adiciona a transcrição ao objeto de vídeo."""
        raw_transcript = TranscriptService.get_transcript(video.id)
        if raw_transcript:
            transcript_items = [
                TranscriptItem(text=item['text'], start=item['start'], duration=item['duration'])
                for item in raw_transcript
            ]
            video.transcript = transcript_items
        return video

    @staticmethod
    def add_transcripts_to_playlist(playlist: Playlist) -> Playlist:
        """Adiciona transcrições a todos os vídeos na playlist."""
        for i, video in enumerate(playlist.videos):
            playlist.videos[i] = TranscriptService.add_transcript_to_video(video)
        return playlist