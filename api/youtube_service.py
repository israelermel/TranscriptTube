import pytube
from typing import List, Tuple, Optional
from models.data_models import Video, Playlist
from utils.url_utils import extract_video_id


class YouTubeService:
    @staticmethod
    def get_video_title(video_id: str) -> str:
        """Obtém o título do vídeo."""
        return f"Video_{video_id}"

    @staticmethod
    def get_video_details(video_id: str) -> Video:
        """Retorna o objeto Video com o título."""
        title = YouTubeService.get_video_title(video_id)
        return Video(id=video_id, title=title)

    @staticmethod
    def get_playlist_videos(playlist_id: str) -> Tuple[List[str], str]:
        """Obtém todos os vídeos de uma playlist."""
        try:
            playlist = pytube.Playlist(f'https://www.youtube.com/playlist?list={playlist_id}')
            video_ids = []

            for url in playlist.video_urls:
                video_id = extract_video_id(url)
                if video_id and not isinstance(video_id, tuple):
                    video_ids.append(video_id)

            return video_ids, playlist.title
        except Exception as e:
            print(f"Erro ao processar playlist: {str(e)}")
            return [], f"Playlist_{playlist_id}"

    @staticmethod
    def get_playlist_details(playlist_id: str) -> Playlist:
        """Retorna o objeto Playlist com todos os vídeos."""
        video_ids, playlist_title = YouTubeService.get_playlist_videos(playlist_id)

        videos = []
        for video_id in video_ids:
            video = YouTubeService.get_video_details(video_id)
            videos.append(video)

        return Playlist(id=playlist_id, title=playlist_title, videos=videos)
