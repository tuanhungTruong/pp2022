import os
import re

while True:
    cur_dir = os.getcwd()
    command = input(">")
    if command.split()[0] == "cd":
        try:
            os.chdir(command[3:])
        except FileNotFoundError:
            print("bash: cd: No such file or directory")
    elif command == 'exit':
        break
    elif command == 'bc':
        while True:
            if os.path.isfile("file.txt") == False:
                open('file.txt', 'a').close()
            file = open('file.txt', 'a')
            get_input = input("bc < ")
            file.write(get_input + "\n")
            file.close()
            print("Do you wish to continue ? yes or no \n")
            command1 = input("bc > ")
            if command1 == "no":
                break
            if command1 == "yes":
                print("\n")              

    elif command == "ls -la":
        command2 = input("ls -la > ")
        if os.path.isfile(command2) == False:
            print("bash: error: Can not find a file name " + command2)
        else:    
            file = open(command2, 'r')
            print(file.read())

    elif command == "ps aux":
        onlyfiles = [f for f in os.listdir(cur_dir) if os.path.isfile(os.path.join(cur_dir, f))]
        command2 = input("ps aux >")
        for file in onlyfiles:
            file1 = open(file, "r")
            for word in file1:
                if re.search(command2, word):
                    print("The word " + command2 + " is in the " + file1.name + " file")
    else:
        os.system(command)