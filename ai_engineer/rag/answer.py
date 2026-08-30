from ai_engineer.rag.retriever import Retriever
from ai_engineer.llm.client import generate

def answer_question(question):
    results=Retriever().search(question)
    if not results: return {'answer':'No grounded answer found.','sources':[]}
    context='\n\n'.join(r['content'][:1200] for r in results)
    first=results[0]['content'].replace('#','').strip().split('\n')[:4]
    fallback=' '.join(x.strip() for x in first if x.strip())
    prompt=f'Answer only from the provided context.\n\n{context}\n\nQuestion: {question}'
    return {'answer':generate(prompt,fallback=fallback),'sources':[r['source'] for r in results]}
