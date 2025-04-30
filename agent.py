from transcript_utils import get_transcript
from search_utils import search_transcript

def run_agent(video_url, prompt):
    try:
        transcript = get_transcript(video_url)
    except Exception as e:
        print("❌ Failed to get transcript:", e)
        return []

    matches = search_transcript(transcript, prompt, top_k=5)
    return matches
