def contains_expected(answer,expected):
    if not expected: return 1.0
    a=answer.lower(); return sum(1 for x in expected if x.lower() in a)/len(expected)
def route_accuracy(expected_route,actual_route): return 1.0 if expected_route==actual_route else 0.0
