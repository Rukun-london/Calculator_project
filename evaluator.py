def is_number(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

def apply_operator(op,left,right):
    if op=="+":
        return left+right
    elif op=="-":
        return left-right
    elif op=="*":
        return left*right
    elif op=="/":
        if right==0:
            raise ZeroDivisionError("division by zero")
        return left/right
    elif op=="%":
        if right==0:
            raise ZeroDivisionError("division by zero")
        return left%right
    elif op=="^" or op=="exp":
        return left**right
    else:
        raise ValueError(f"Invalid operator {op}")
precedence = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
    "%": 2,
    "^": 3,
    "exp": 3
}
OPERATORS={
    '+': {"precedence": 1, "associativity": "left"},
    '-': {"precedence": 1, "associativity": "left"},
    '*': {"precedence": 2, "associativity": "left"},
    '/': {"precedence": 2, "associativity": "left"},
    '%': {"precedence": 2, "associativity": "left"},
    '^': {"precedence": 3, "associativity": "right"},
    'exp': {"precedence": 3, "associativity": "right"}

}
# example: 3 + 4 * 2 ^ 5
def evaluate(tokens):
    values=[]
    operators=[]
    i=0
    while i<len(tokens):
        token=tokens[i]
        if is_number(token):
            values.append(float(token))
        elif token=="(":
            operators.append(token)
        elif token==")":
            while operators and operators[-1]!="(":
                apply_top_operator(values,operators)
                operators.pop()
        else:
            while operators and operators[-1]!="(" and precedence[operators[-1]]>precedence[token]:
                apply_top_operator(values,operators)
            operators.append(token)
        i=i+1
    while operators:
        apply_top_operator(values,operators)

    return values[0]


def apply_top_operator(values,operators):
    right=values.pop()
    left=values.pop()
    op=operators.pop()
    result=apply_operator(op,left,right)
    values.append(result)


# while
#
#     tokens=tokens[:]
#     operator_levels=[
#         ["^","exp"],
#         ["*","/","%"],
#         ["+","-"]
#     ]
#     for operators in operator_levels:
#         i=0
#         while i<len(tokens):
#             token=tokens[i]
#             if token in operators:
#                 if i==0 or i==len(tokens)-1:
#                     raise ValueError(f"Invalid expression structure")
#                 left=float(tokens[i-1])
#                 right=float(tokens[i+1])
#                 result=apply_operator(token,left,right)
#                 tokens[i-1:i+2]=[str(result)]
#                 i=0
#             else:
#                 i+=1
#     if len(tokens)!=1:
#         raise ValueError(f"Invalid expression ")
#     return float(tokens[0])

