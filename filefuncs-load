import shutil
import os
from pathlib import Path
# 1. CREATE A FILE
def create_file(filename):
    Path(filename).touch(exist_ok=True)
# 2. WRITE TO A FILE (overwrites existing content)
def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
# 3. APPEND TO A FILE (adds content without deleting existing content)
def append_file(filename, content):
    with open(filename, "a", encoding="utf-8") as file:
        file.write(content)
# 4. READ A FILE
def read_file(filename):
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    else:
        print("File does not exist.", file=sys.stderr)
        return None
# 5. COPY A FILE
def copy_file(source, destination):
    if os.path.isfile(source):
        shutil.copy2(source, destination)
    else:
        print("Source file does not exist.", file=sys.stderr)
# 6. MOVE A FILE
def move_file(source, destination):
    if os.path.exists(source):
        shutil.move(source, destination)
    else:
        print("Source does not exist.", file=sys.stderr)
# 7. RENAME A FILE
def rename_file(old_name, new_name):
    if os.path.exists(old_name):
        os.rename(old_name, new_name)
    else:
        print("File does not exist.", file=sys.stderr)
# 8. DELETE A FILE
def delete_file(filename):
    if os.path.isfile(filename):
        os.remove(filename)
    else:
        print("File does not exist.", file=sys.stderr)
# 9. CREATE A DIRECTORY
def create_directory(directory):
    os.makedirs(directory, exist_ok=True)
# 10. DELETE A DIRECTORY (including its contents)
def delete_directory(directory):
    if os.path.isdir(directory):
        shutil.rmtree(directory)
    else:
        print("Directory does not exist.", file=sys.stderr)
# 11. LIST DIRECTORY CONTENTS
def list_directory(directory="."):
    if os.path.isdir(directory):
        for item in os.listdir(directory):
            print(item)
    else:
        print("Directory does not exist.", file=sys.stderr)
# 12. CHECK IF A FILE OR DIRECTORY EXISTS
def check_exists(path):
    if os.path.exists(path):
        return True
    else:
        return False
# CMDLIST:
# create_file
# write_file
# append_file
# read_file
# copy_file
# move_file
# rename_file
# delete_file
# create_directory
# delete_directory
# list_directory
# check_exists
