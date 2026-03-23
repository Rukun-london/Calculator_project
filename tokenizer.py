import re
def tokenize(expression):
    expression = expression.replace(" ", "")
    expression=re.sub(r'(\d+)(\()',r'\1*\2',expression)
    expression=re.sub(r'(\))(\d+)',r'\1*\2',expression)
    expression=re.sub(r'(\))(\()',r'\1*\2',expression)
    expression=re.sub(r'\(-',r'(0-',expression)
    expression=re.sub(r'\*-', '*0-',expression)
    expression=re.sub(r'exp',r' exp ',expression)
    if expression and expression[0]=='-':
        expression= '0' + expression

    expression=re.sub(r'\s*((exp)|([+\-*/()%^]))\s*',r' \1 ',expression).lower()
    expression=' '.join(expression.split())
    return expression.split()
if __name__=='__main__':
    tests=[
    "3-5",
    "3(4*-2)",
    "-(2+3)-3 exp4"

    ]
    for test in tests:
        print("original: ", test)
        result=tokenize(test)
        print(result)
        print()
