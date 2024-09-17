import os
import shutil

def move_files(source_folder, destination_folder):
    # Check if the source folder exists
    if not os.path.exists(source_folder):
        print(f"The source folder '{source_folder}' does not exist.")
        return

    # Check if the destination folder exists, create it if it doesn't
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
        print(f"Created destination folder '{destination_folder}'.")

    # List all files in the source folder
    files = os.listdir(source_folder)

    # Move each file to the destination folder
    for file_name in files:
        source_file = os.path.join(source_folder, file_name)
        destination_file = os.path.join(destination_folder, file_name)

        # Check if it's a file before moving
        if os.path.isfile(source_file):
            shutil.move(source_file, destination_file)
            print(f"Moved: {file_name}")

if __name__ == "__main__":
    # Define the source and destination folders
    desktop_folder = os.path.expanduser("~/Desktop")
    destination_folder = os.path.expanduser("~/Documents/MovedFiles")

    # Move files from Desktop to the destination folder
    move_files(desktop_folder, destination_folder)