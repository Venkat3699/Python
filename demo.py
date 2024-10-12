
colours = ["black", "red", "green", "orange", "white"]

for colour in colours: 
    print (colour)
    
print ("While loop")

colours = ["black", "red", "green", "orange", "white"]
index = 0
while index < len(colours):
    print (colours[index])
    index += 1    
    
    
print ("break for statement")
colours = ["black", "red", "green", "orange", "white"]
for colour in colours:
    if colour == "green":
        break
    print (colour)
    
print ("break while statement")
colours = ["black", "red", "green", "orange", "white"]
index = 0
while index < len(colours):
    print (colours[index])
    if colours[index] == "green":
        break
    index += 1
    
print("continue for statement")
colours = ["black", "red", "green", "orange", "white"]
for colour in colours:
    if colour == "green":
        continue
    print (colour)
    
print("continue for while statement")
colours = ["black", "red", "green", "orange", "white"]
index = 0
while index < len(colours):
    if colours[index] == "green":
        index += 1
        continue
    print (colours[index])
    index += 1