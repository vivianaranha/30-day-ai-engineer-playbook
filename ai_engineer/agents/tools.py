CUSTOMERS={'northstar bank':{'industry':'Financial Services','opportunity':'AI customer-service modernization','priority':'High'},'acme retail':{'industry':'Retail','opportunity':'Store operations assistant','priority':'Medium'}}
def customer_lookup(name): return CUSTOMERS.get(name.lower(),{'error':'Customer not found'})
def calculator(a,b,op):
    if op=='add': return a+b
    if op=='subtract': return a-b
    if op=='multiply': return a*b
    if op=='divide':
        if b==0: raise ValueError('Division by zero')
        return a/b
    raise ValueError('Unsupported operation')
