import sys
import os

PATH = os.environ.get("PATH")

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command == "exit 0":
            break
        elif command.startswith('echo'):
            command = command.split()
            print(" ".join(command[1:]))
        elif command.startswith('type'):
            PATH = PATH.split(':')
            command = command.split()
            for bin in PATH:
                if os.path.isfile(f'{bin}/{command[1]}'):
                    cmd = f'{bin}/{command[1]}'
            if command[1] in ['echo', 'exit', 'type']:
                print("".join(f'{command[1]} is a shell builtin'))
            elif command[1]:
                print(f'{command[1]}is {cmd}')

        else:
            print(f"{command}: command not found")
if __name__ == "__main__":
    main()