import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge 2 dollers per day")
elif type == "t2.medium":
    print("it will charge 4 dollers per day")
elif type == "t2.xlarge":
    print("it will charge 8 dollers per day")
else:
    print("Please, provide the valid instance type")

# Command: python if_else.py t2.micro
# Output: it will charge 2 dollers per day

# Command: python if_else.py t2.medium
# Output: it will charge 4 dollers per day

# Command: python if_else.py t2.xlarge
# Output: it will charge 8 dollers per day

# Command: python if_else.py t2.xeh
# Output: Please, provide the valid instance type