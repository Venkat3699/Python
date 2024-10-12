colours = ["black", "red", "green", "orange", "white"]
index = 0
while index < len(colours):
    if colours[index] == "green":
        index += 1
        continue
    print (colours[index])
    index += 1