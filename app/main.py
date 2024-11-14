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
            print(f" ".join(command[1:]))
        elif command.startswith('type'):
            paths = PATH.split(':')
            command = command.split()[1]
            command_path = None
            for path in paths:
                if os.path.isfile(f'{path}/{command}'):
                    command_path = f'{path}/{command}'
            if command in ['echo', 'exit', 'type', 'pwd', 'cd']:
                print(f'{command} is a shell builtin')
            elif command_path:
                print(f'{command} is {command_path}')
            else:
                print(f"{command}: not found")
        elif command == 'pwd':
            print(os.getcwd())
        elif command.split()[0] == 'cd':
            if os.path.isdir(command.split()[1]):
                prev_dir = os.getcwd()
                os.chdir(command.split()[1])
            elif command.split()[1] == '../':
                os.chdir(prev_dir)
            elif command.split()[1] == '~':
                home_dir = os.path.expanduser('~')
                os.chdir(home_dir)
            else:
                print(f'{command.split()[0]}: {command.split()[1]}: No such file or directory')
        elif command:
            paths = PATH.split(':')
            command_name = command.split()[0]
            command_found = any(os.path.isfile(f'{path}/{command_name}') for path in paths)

            if command_found:
                os.system(command)
            else:
                print(f"{command_name}: command not found")
        else:
            print(f"{command.split()[0]}: command not found")

if __name__ == "__main__":
    main()