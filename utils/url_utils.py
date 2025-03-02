from urllib.parse import urlparse, parse_qs

def extract_video_id(url):
    """Extrai o ID do vídeo ou playlist a partir da URL do YouTube."""
    parsed_url = urlparse(url)

    if 'youtube.com' in parsed_url.netloc:
        if 'v' in parse_qs(parsed_url.query):
            return parse_qs(parsed_url.query)['v'][0]
        elif 'list' in parse_qs(parsed_url.query):
            return parse_qs(parsed_url.query)['list'][0], 'playlist'
        elif 'watch' in parsed_url.path and '/watch/' in parsed_url.path:
            return parsed_url.path.split('/watch/')[1]
    elif 'youtu.be' in parsed_url.netloc:
        return parsed_url.path[1:]

    return None