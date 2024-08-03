import os
import shutil

# Directory to be emptied
TARGET_DIR = os.path.expanduser("~/Pictures/Screenshots")

def empty_folder(directory):
    if os.path.exists(directory) and os.path.isdir(directory):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print(f'Failed to delete {file_path}. Reason: {e}')
        print(f'The folder {directory} has been emptied.')
    else:
        print(f'The folder {directory} does not exist.')

if __name__ == "__main__":
    empty_folder(TARGET_DIR)
