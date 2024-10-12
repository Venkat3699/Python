# Example using For statement

numbers = [1, 2, 3, 4, 5]

for number in numbers:
    if number == 3:
        break
    print(number)
else: 
    print ("execution failed")
    
# Example using while statement

print ("Example using while statement")
i = 1
while i < 6:
    print (i)
    if i == 3:
        break
    i += 1

# Example2 using while statement

print ("Example2 using while statement")
colours = ["red", "green", "yellow", "blue", "orange"]
index = 0
while index < len(colours):
    print (colours[index])
    if colours[index] == "yellow":
        break
    index += 1