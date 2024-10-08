# Examples for "in" Operator

fruit = ["apple", "banana", "mango"]
result = "banana" in fruit
print ("fruit is matched in given list:", result)

colour = ["red", "white", "black"]
result = "red" in colour
print ("colour is matched in given list:", result)

result = "orange" in fruit
print ("Fruit is matched in the list:", result)

result = "green" in colour
print ("colour is matched in the list:", result)

# Examples of "not in" Operator

fruit = ["apple", "banana", "mango"]
result = "banana" not in fruit
print ("fruit is matched in given list for not in:", result)
 
colour = ["red", "white", "black"]
result = "red" not in colour
print ("colour is matched in given list for not in:", result)

result = "orange" not in fruit
print ("Fruit is matched in the list for not in:", result)

result = "green" not in colour
print ("colour is matched in the list for not in:", result)