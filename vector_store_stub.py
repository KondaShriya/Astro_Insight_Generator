from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

CORPUS = [
    ("leadership", "Your leadership aura helps in team settings."),
    ("finance", "Careful budgeting today helps you avoid surprises."),
    ("relationships", "Honest talk clears tension."),
]

class MockVectorStore:
    def __init__(self):
        self.texts = [t for k, t in CORPUS]
        self.keys = [k for k, t in CORPUS]
        self.vectorizer = TfidfVectorizer().fit(self.texts)
        self.vectors = self.vectorizer.transform(self.texts)

    def retrieve(self, query: str, top_k: int = 1):
        qv = self.vectorizer.transform([query])
        sims = cosine_similarity(qv, self.vectors)[0]
        idxs = np.argsort(sims)[::-1][:top_k]
        return [(self.keys[i], self.texts[i], float(sims[i])) for i in idxs]
