from agent import run_agent

if __name__ == __main__:
    video_url = input(Enter YouTube video URL: ).strip()
    user_prompt = input(What are you looking for in the video? ).strip()

    results = run_agent(video_url, user_prompt)

    print(n--- Matching Timestamps ---)
    for r in results:
        print(f"[{r[start]:.2f}s] {r[text]}")

