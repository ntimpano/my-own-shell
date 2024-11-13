import sys
import os



def main():
    while True:
        PATH = os.environ.get("PATH")
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input()
        if command == "exit 0":
            break
        elif command.startswith('echo'):
            command = command.split()
            print(" ".join(command[1:]))
        elif command.startswith('type'):
            paths = PATH.split(':')
            command_path = None
            command = command.split()[1]
            for path in paths:
                if os.path.isfile(f'{path}/{command}'):
                    command_path = f'{path}/{command}'
            if command in ['echo', 'exit', 'type']:
                print(f'{command} is a shell builtin')
            elif command_path:
                print(f'{command} is {command_path}')
            else:
                print(f"{command}: command not found")
        else:
            print(f"{command}: command not found")
if __name__ == "__main__":
    main()