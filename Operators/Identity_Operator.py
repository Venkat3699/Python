# is: Returns True if both operands refer to the same object.
# is not: Returns True if both operands refer to different objects.

# Examples

x = [1, 2, 3]
y = x
result = x is y
print ("output of X is y values:", result)

result = x is not y
print ("output of X is not y values:", result)

# Example 2

a = "hello"
b = "world"

result = a is b
print ("output of a is b values:", result)

result = a is not b
print("output of a is not b values:", result)