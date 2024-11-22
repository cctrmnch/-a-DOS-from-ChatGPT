import os
import time
import shutil
import fnmatch

def start_msdos():
    current_drive = "C:"
    current_dir = os.getcwd()
    print("A-DOS Version 6.22")
    print("A-DOS Project, 1981-2024.")
    print("Type HELP for a list of commands.")
    print()

    while True:
        command = input(f"{current_drive}\\{current_dir}> ").strip().lower()

        if command == "help":
            show_help()
        elif command == "cls":
            os.system('cls' if os.name == 'nt' else 'clear')
        elif command.startswith("dir"):
            dir_command(command, current_dir)
        elif command.startswith("cd"):
            current_dir = change_directory(command, current_dir)
        elif command.startswith("mkdir"):
            make_directory(command[6:], current_dir)
        elif command.startswith("rmdir"):
            remove_directory(command[6:], current_dir)
        elif command.startswith("del"):
            delete_file(command[4:], current_dir)
        elif command.startswith("copy"):
            copy_file(command[5:], current_dir)
        elif command.startswith("move"):
            move_file(command[5:], current_dir)
        elif command.startswith("edit"):
            edit_file(command[5:], current_dir)
        elif command == "chkdsk":
            chkdsk_command(current_dir)
        elif command.startswith("format"):
            format_command(command[7:], current_dir)
        elif command == "exit":
            print("Exiting MS-DOS...")
            time.sleep(1)
            break
        else:
            print(f"'{command}' is not recognized as an internal or external command.")

# Command: HELP
def show_help():
    print("Commands Available in A-DOS Simulation:")
    print("CLS          : Clears the screen.")
    print("DIR          : Lists files and directories with wildcard support.")
    print("CD           : Changes the directory.")
    print("MKDIR        : Creates a new directory.")
    print("RMDIR        : Removes an empty directory.")
    print("DEL          : Deletes a file.")
    print("COPY         : Copies a file.")
    print("MOVE         : Moves a file to another directory.")
    print("EDIT         : Edits or creates a text file.")
    print("CHKDSK       : Checks disk for errors.")
    print("FORMAT       : Formats a virtual disk.")
    print("EXIT         : Exits A-DOS simulation.")

# Command: DIR
def dir_command(command, current_dir):
    args = command[3:].strip()
    pattern = "*" if not args else args
    print(f"Directory of {current_dir} \n")
    total_files = 0
    total_size = 0
    with os.scandir(current_dir) as entries:
        for entry in entries:
            if fnmatch.fnmatch(entry.name, pattern):
                if entry.is_file():
                    size = entry.stat().st_size
                    print(f"{entry.name:20} {size} bytes")
                    total_files += 1
                    total_size += size
                elif entry.is_dir():
                    print(f"{entry.name:20} <DIR>")
    print(f"\n{total_files} File(s) {total_size} bytes")

# Command: CD
def change_directory(command, current_dir):
    path = command[3:].strip()
    if path == "..":
        return os.path.dirname(current_dir)
    else:
        new_dir = os.path.join(current_dir, path)
        if os.path.exists(new_dir) and os.path.isdir(new_dir):
            return new_dir
        else:
            print(f"The system cannot find the path specified: {path}")
            return current_dir

# Command: MKDIR
def make_directory(dirname, current_dir):
    path = os.path.join(current_dir, dirname)
    try:
        os.mkdir(path)
        print(f"Directory created: {dirname}")
    except Exception as e:
        print(f"Error creating directory: {e}")

# Command: RMDIR
def remove_directory(dirname, current_dir):
    path = os.path.join(current_dir, dirname)
    try:
        os.rmdir(path)
        print(f"Directory removed: {dirname}")
    except Exception as e:
        print(f"Error removing directory: {e}")

# Command: DEL
def delete_file(filename, current_dir):
    path = os.path.join(current_dir, filename)
    try:
        os.remove(path)
        print(f"File deleted: {filename}")
    except Exception as e:
        print(f"Error deleting file: {e}")

# Command: COPY
def copy_file(args, current_dir):
    try:
        src, dest = args.split()
        shutil.copy(os.path.join(current_dir, src), os.path.join(current_dir, dest))
        print(f"Copied {src} to {dest}")
    except Exception as e:
        print(f"Error copying file: {e}")

# Command: MOVE
def move_file(args, current_dir):
    try:
        src, dest = args.split()
        shutil.move(os.path.join(current_dir, src), os.path.join(current_dir, dest))
        print(f"Moved {src} to {dest}")
    except Exception as e:
        print(f"Error moving file: {e}")

# Command: EDIT
def edit_file(filename, current_dir):
    path = os.path.join(current_dir, filename)
    try:
        if os.path.exists(path):
            print(f"Editing file: {filename}\n")
            with open(path, 'r') as file:
                print(file.read())
        print("Enter new content for the file (Ctrl+C to save and exit):")
        with open(path, 'w') as file:
            while True:
                line = input()
                file.write(line + '\n')
    except KeyboardInterrupt:
        print("\nFile saved.")

# Command: CHKDSK
def chkdsk_command(current_dir):
    print("Checking disk...")
    print("No errors found.")
    print(f"Current directory: {current_dir}")

# Command: FORMAT
def format_command(drive, current_dir):
    print(f"Formatting drive {drive}...")
    print("Format complete.")

if __name__ == "__main__":
    start_msdos()
