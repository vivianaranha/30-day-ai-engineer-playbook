from ai_engineer.evaluation.metrics import contains_expected,route_accuracy
def test_contains_expected(): assert contains_expected('Submit within 30 days',['30 days'])==1.0
def test_route_accuracy(): assert route_accuracy('knowledge','knowledge')==1.0
