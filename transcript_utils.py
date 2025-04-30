from youtube_transcript_api import YouTubeTranscriptApi
import re

def extract_video_id(url):
    match = re.search(r"(?:v=|youtu\.be/)([\w-]+)", url)
    if match:
        return match.group(1)
    raise ValueError("Could not extract video ID.")

def get_transcript(url):
    video_id = extract_video_id(url)
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    return transcript  # list of dicts: {text, start, duration}
