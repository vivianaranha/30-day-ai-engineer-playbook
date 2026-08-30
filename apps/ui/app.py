import streamlit as st
from ai_engineer.agents.agent import AIAssistant
from ai_engineer.security.guardrails import detect_prompt_injection
st.set_page_config(page_title='30-Day AI Engineer Playbook',layout='wide')
st.title('Enterprise AI Assistant')
st.caption('RAG + tools + routing + evaluation-ready architecture')
a=AIAssistant(); examples=['What is the travel reimbursement policy?','Tell me about Northstar Bank','Multiply 12 and 7']
selected=st.selectbox('Example',['']+examples); custom=st.text_input('Ask a question'); query=custom or selected
if st.button('Run',disabled=not bool(query)):
    if detect_prompt_injection(query): st.error('Request blocked by security policy.')
    else:
        r=a.run(query); st.write('### Route'); st.code(r['route']); st.write('### Answer'); st.write(r['answer'])
        if r.get('sources'):
            st.write('### Sources')
            for s in r['sources']: st.write(f'- {s}')
