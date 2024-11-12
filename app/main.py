import sys
import subprocess


def main():
    while True:

        sys.stdout.write("$ ")
        sys.stdout.flush()

        command = input()
        status = subprocess.run(command, capture_output=True)
        if status.returncode != 0:
            sys.stdout.write(f"{command}: command not found\n")
            sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
