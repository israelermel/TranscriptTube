# api/transcript_service.py
from youtube_transcript_api import YouTubeTranscriptApi, _errors
from typing import List, Optional
from models.data_models import TranscriptItem, Video, Playlist


class TranscriptService:
    @staticmethod
    def get_transcript(video_id: str, languages: List[str] = None) -> Optional[List[dict]]:
        """Obtém a transcrição do vídeo usando a API de transcrição do YouTube.

        Args:
            video_id: ID do vídeo do YouTube
            languages: Lista de códigos de idioma para tentar obter a transcrição,
                       por ordem de preferência

        Returns:
            Lista de segmentos de transcrição ou None se não encontrar
        """
        if languages is None or len(languages) == 0:
            # Padrão: tenta primeiro português, depois inglês
            languages = ['pt', 'en']

        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            return transcript
        except _errors.NoTranscriptFound:
            print(f"Nenhuma transcrição encontrada para o vídeo ID: {video_id} nos idiomas: {languages}")
            return None
        except Exception as e:
            print(f"Erro ao obter transcrição: {str(e)}")
            return None

    @staticmethod
    def list_available_transcripts(video_id: str) -> List[dict]:
        """Lista todas as transcrições disponíveis para um vídeo.

        Args:
            video_id: ID do vídeo do YouTube

        Returns:
            Lista de dicionários com informações das transcrições disponíveis
        """
        try:
            transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

            available_transcripts = []
            for transcript in transcript_list:
                transcript_info = {
                    'language_code': transcript.language_code,
                    'language': transcript.language,
                    'is_generated': transcript.is_generated,
                    'is_translatable': transcript.is_translatable
                }
                available_transcripts.append(transcript_info)

            return available_transcripts
        except Exception as e:
            print(f"Erro ao listar transcrições disponíveis: {str(e)}")
            return []

    @staticmethod
    def add_transcript_to_video(video: Video, languages: List[str] = None) -> Video:
        """Adiciona a transcrição ao objeto de vídeo.

        Args:
            video: Objeto Video a ser atualizado
            languages: Lista de códigos de idioma para tentar obter a transcrição

        Returns:
            Objeto Video atualizado com a transcrição
        """
        raw_transcript = TranscriptService.get_transcript(video.id, languages)
        if raw_transcript:
            transcript_items = [
                TranscriptItem(text=item['text'], start=item['start'], duration=item['duration'])
                for item in raw_transcript
            ]
            video.transcript = transcript_items
        return video

    @staticmethod
    def add_transcripts_to_playlist(playlist: Playlist, languages: List[str] = None) -> Playlist:
        """Adiciona transcrições a todos os vídeos na playlist.

        Args:
            playlist: Objeto Playlist a ser atualizado
            languages: Lista de códigos de idioma para tentar obter as transcrições

        Returns:
            Objeto Playlist atualizado com transcrições
        """
        for i, video in enumerate(playlist.videos):
            playlist.videos[i] = TranscriptService.add_transcript_to_video(video, languages)
        return playlist