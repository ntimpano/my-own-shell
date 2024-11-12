import sys


def main():

    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        valid_command = []
        command = input()
        if command not in valid_command:
            print(f"{command}: command not found\n")
            continue


if __name__ == "__main__":
    main()
