import os

def main():
    folders = input("Please provide the list of folder names with space between:").split()
    for folder in folders:
        if os.path.isdir(folder):
            files = os.listdir(folder)
            if files:
                print ("list of files in folder", folder)
                for file in files:
                    print(file)
            else:
                print(f"folder '{folder}' is not available")
        else: 
            print(f"folder '{folder}' is not available, please provide the vaild folder name")
            break
main ()