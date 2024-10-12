# Example using For Statement

fruits = ["grapes", "apple", "banana", "orange"]
for fruit in fruits:
    if fruit == "apple":
        continue
    print(fruit)
    
# Example using While Statement

print ("Example using While Statement")
fruits = ["grapes", "apple", "banana", "orange"]
index = 0
while index < len(fruits):
    
    if fruits[index] == "banana":
        index += 1
        continue
    print (fruits[index])
    index += 1