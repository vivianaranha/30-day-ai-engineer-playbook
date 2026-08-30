def route(query):
    t=query.lower()
    if any(x in t for x in ['policy','document','knowledge','reimbursement']): return 'knowledge'
    if any(x in t for x in ['customer','account','northstar','acme']): return 'customer'
    if any(x in t for x in ['calculate','multiply','divide','*']): return 'calculator'
    return 'general'
