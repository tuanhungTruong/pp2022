
import os

while True:
    command = input(">")
    if command.split()[0] == "cd":
        try:
            os.chdir(command[3:])
        except FileNotFoundError:
            print("bash: cd: No such file or directory")
    elif command == 'exit':
        break
    else:
        os.system(command)