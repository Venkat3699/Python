import os

def main():
    folders = input("please provide the list of folder names with space between:").split()
    for folder in folders:
        try:
            files = os.listdir(folder)
        except FileNotFoundError:
            print ("Please provide a valid folder name")
            break
        print("lisiting of file names in folder =" + folder)
        
        for file in files:
            print (file)

main()