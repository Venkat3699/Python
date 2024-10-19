import os
def main():
    folders = input("Please provide a list of folders with space between: ").split()
    for folder in folders:
        if os.path.isdir(folder):  # Check if the folder exists
            files = os.listdir(folder)
            if files:
                print("List of files in folder:", folder)
                for file in files:
                    print(file)
            else:
                print(f"Folder '{folder}' is empty")
                
        else:
            print(f"Folder '{folder}' does not exist. Please provide a valid folder name.")
            break  # Break the loop if an invalid folder is found

if __name__ == "__main__":
    main()