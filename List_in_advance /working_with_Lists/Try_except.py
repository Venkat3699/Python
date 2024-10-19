import os

folders = input ("please provide a list of folder names with space between:").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except:
        print("please provide a valid folder name")
        break
    print("===Listing of files in folder: " + folder)
    
    for file in files:
        print (file)
        
# Provide 2 inputs as /opt and /xyz