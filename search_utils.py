from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

def search_transcript(transcript, query, top_k=5):
    texts = [entry["text"] for entry in transcript]
    embeddings = model.encode(texts, convert_to_tensor=True)
    query_emb = model.encode(query, convert_to_tensor=True)

    scores = util.pytorch_cos_sim(query_emb, embeddings)[0]
    top_results = scores.topk(top_k)

    matches = []
    for idx in top_results.indices:
        idx = idx.item()
        matches.append({
            "text": transcript[idx]["text"],
            "start": transcript[idx]["start"],
            "score": scores[idx].item()
        })
    return matches
