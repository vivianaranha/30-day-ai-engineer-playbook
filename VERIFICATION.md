# Verification

## Python compilation
PASS

## Automated tests
PASS

```text
.............                                                            [100%]
13 passed in 3.01s

```

## Data preparation
PASS

```text
Loaded 5 rows
 id            text          label
  1     login issue authentication
  2 invoice problem        billing
  3 network latency        network
  4  password reset authentication
  5  refund request        billing
```

## Evaluation script
PASS

```text
{'query': 'What is the travel reimbursement policy?', 'task_score': 1.0, 'route_score': 1.0}
{'query': 'Tell me about Northstar Bank', 'task_score': 1.0, 'route_score': 1.0}
{'query': 'Multiply 12 and 7', 'task_score': 1.0, 'route_score': 1.0}
```

## Agent smoke test
PASS

```text
QUERY: What is the travel reimbursement policy?
{'route': 'knowledge', 'answer': 'Travel Reimbursement Policy Employees should submit business travel expenses within 30 days after completing travel. Airfare should normally be booked in economy class unless an approved exception applies. Receipts are required for hotel, ground transportation, and other material expenses.', 'sources': ['knowledge/hr/travel-policy.md', 'knowledge/security/ai-policy.md']}

QUERY: Tell me about Northstar Bank
{'route': 'customer', 'answer': "{'industry': 'Financial Services', 'opportunity': 'AI customer-service modernization', 'priority': 'High'}", 'sources': []}

QUERY: Multiply 12 and 7
{'route': 'calculator', 'answer': '84.0', 'sources': []}
```
