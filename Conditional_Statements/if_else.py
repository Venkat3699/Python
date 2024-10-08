import sys

type = sys.argv[1]

if type == "t2.micro":
    print("ok, we will create an instance")
else:
    print("you provided wrong instance type, check once")

# Command: python if_else.py t2.micro
# Output: ok, we will create an instance

# Command: python if_else.py t2.medium
# Output: you provided wrong instance type, check once