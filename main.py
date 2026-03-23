from tokenizer import tokenize
from evaluator import evaluate
expressions = [
    "3+4*2",
    "(3+4)*2",
    "3+4*2-1",
    "10/2+3",
    "2 + 3 * 4",
    "10 - 2 * 3",
    "2 exp 3 + 1",
]
for expression in expressions:
    tokens=tokenize(expression)
    result=evaluate(tokens)
    print(f"Result: ",result)