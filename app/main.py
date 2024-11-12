import sys
import subprocess


def main():
    # Uncomment this block to pass the first stage
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command = input()
    command = command.split()
    status = subprocess.run([command], capture_output=True)
    if status.returncode != 0:
        sys.stdout.write(f"{command}: command not found\n")
        sys.stdout.write("$ ")


if __name__ == "__main__":
    main()
