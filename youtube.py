import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from youtube_transcript_api import YouTubeTranscriptApi

language_codes = [
    "en", "es", "zh", "hi", "fr", "ar", "pt", "ru", "id", "de",
    "ja", "jv", "vi", "ko", "te", "mr", "ta", "ur", "tr", "gu",
    "pl", "bn", "pa", "zh", "ml", "th", "fa", "zh", "zh", "it",
    "ar", "ba", "bh", "zh", "ilo", "my", "zh", "fu", "ms", "su",
    "uz", "sd", "am", "az", "ku", "ps", "ctg", "rw", "ha", "or",
    "as", "si", "ig", "ne", "no", "ms", "ceb", "nl", "zh", "sn",
    "hau", "zu", "sv", "hmn", "mai", "uk", "cy", "zh", "qro",
    "ar", "ar", "vm", "be", "bs", "bei", "ky", "ug", "ti",
    "az", "brh", "lmo", "sk", "kab", "lo", "tg", "hu", "dhd",
    "rm", "ctu", "ce", "el", "pam", "tl", "xal", "km", "mt",
    "mk", "sga", "sw", "br", "lzh", "mhr", "az", "pi", "mai",
    "scn", "sw", "br", "lt", "zh", "ar", "ar", "fo", "be",
    "nov", "az", "mzn", "ky", "ug", "ti", "zh-CN", "yue", "zh-wuu",
    "zh-min-nan", "hak", "zh-gan"
]

def is_youtube(url):
    parsed = urlparse(url)
    return parsed.netloc in ['www.youtube.com', 'youtube.com']

def is_playable(video_id):
    try:
        url = f"https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v={video_id}&format=json"
        resp = requests.get(url)
        resp.raise_for_status()

        return resp.json().get("title") is not None
    except requests.exceptions.HTTPError as err:
        # print(f"HTTP Error: {err}")
        return False
    except requests.exceptions.RequestException as err:
        # print(f"Error: {err}")
        return False

def get_title(video_id):
    try:
        url = f"https://www.youtube.com/watch?v={video_id}"
        resp = requests.get(url)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.content, 'html.parser')
        title_tag = soup.find('title')

        if title_tag:
            return title_tag.text.split("- YouTube")[0].strip()
        else:
            return "No title tag found"

    except requests.exceptions.HTTPError as err:
        # print(f"HTTP Error: {err}")
        return "Title Unavailable"
    except requests.exceptions.RequestException as err:
        # print(f"Error: {err}")
        return "Title Unavailable"

def get_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=language_codes)
        text = ""

        for entry in transcript:
            text += entry['text'] + " "

        return text.strip()
    except Exception as e:
        # print(f"Error: {e}")
        return "Transcript unavailable"