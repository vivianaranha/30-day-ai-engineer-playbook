from ai_engineer.rag.retriever import Retriever
def test_rag_retrieval():
 r=Retriever('knowledge').search('travel reimbursement receipts'); assert r; assert 'travel-policy.md' in r[0]['source']
