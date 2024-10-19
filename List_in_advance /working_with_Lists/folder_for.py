import os
folders = input("Please provide the list of folders names with spaces between:").split()
for folder in folders:
    files = os.listdir(folder)
    print ("======Listing of files for the folder ===== -" + folder)
    print(files) 
for file in files:
    print (file)
    
# Provide 2 inputs as /opt and /tmp