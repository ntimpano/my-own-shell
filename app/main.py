import sys
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        if command == "exit 0":
            break
        elif command.startswith('echo'):
            command = command.split()
            print(" ".join(command[1:]))
        elif command.startswith('type'):
            command = command.split()
            if command[1] in ['echo', 'exit']:
                print("".join(f'{command[1]} is a shell builtin'))
            else:
                print(f'{command[1]}: not found')
        else:
            print(f"{command}: command not found")
if __name__ == "__main__":
    main()