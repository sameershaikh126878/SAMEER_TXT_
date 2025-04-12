import os

def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def clean_up(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
