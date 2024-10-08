import sys

def add(a, b):
    add = a + b
    return add

def sub(a, b):
    sub = a - b
    return sub

def mul(a, b):
    mul = a * b
    return mul

a = int (sys.argv[1])
operation = sys.argv[2]
b = int(sys.argv[3])

if operation == "add":
    output = add(a, b)
    print(output)


if operation == "sub":
    output = sub(a, b)
    print(output)

if operation == "mul":
    output = mul(a, b)
    print(output)

