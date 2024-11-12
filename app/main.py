import sys
import os


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    status = os.system(command)
    if status != 0:
        sys.stdout.write(f"{command}: command not found")
        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
