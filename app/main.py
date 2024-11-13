import sys
def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        # Wait for user input
        command = input()
        if command == "exit 0":
            break
        if command.startswith('echo'):
            command = command.split()
            print(" ".join(command[1:]))
        else:
            print(f"{command}: command not found")
if __name__ == "__main__":
    main()