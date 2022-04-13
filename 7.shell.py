
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
    elif command == 'ls -la':
        while True:
            try:
                if os.path.isfile("file.txt") == False:
                    open('file.txt', 'a').close()
                file = open('file txt', 'a')
                get_input = input(">>")
                file.write(get_input + "\n")
                print("Do you wish to continue ? yes or no \n")
                command1 = input(">>>")
                if command1 == "no":
                    break
                if command1 == "yes":
                    print("\n")              
            except IOError:
                print("Something went wrong")

    else:
        os.system(command)