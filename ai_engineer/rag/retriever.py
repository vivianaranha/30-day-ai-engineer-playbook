from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Retriever:
    def __init__(self, root='knowledge'):
        self.docs=[]
        for p in sorted(Path(root).rglob('*.md')): self.docs.append((str(p),p.read_text(encoding='utf-8')))
        self.vectorizer=self.matrix=None
        if self.docs:
            self.vectorizer=TfidfVectorizer(stop_words='english')
            self.matrix=self.vectorizer.fit_transform([x[1] for x in self.docs])
    def search(self, query, top_k=3):
        if not self.docs: return []
        q=self.vectorizer.transform([query]); scores=cosine_similarity(q,self.matrix)[0]; idx=scores.argsort()[::-1][:top_k]
        return [{'source':self.docs[i][0],'score':float(scores[i]),'content':self.docs[i][1]} for i in idx if scores[i]>0]
