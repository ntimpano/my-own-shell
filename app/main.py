import sys
import subprocess

def main():
    while True:
        # Show prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Read and split the command
        command = input().split()

        if not command:
            continue  # If no command, prompt again

        # Execute the command
        try:
            status = subprocess.run(command, capture_output=True, text=True)
            if status.returncode != 0 or command == 'exit 0':
                # Command failed
                if status.stderr:
                    sys.stdout.write(status.stderr)
                else:
                    sys.stdout.write(f"{command[0]}: command not found\n")
            else:
                # Show command output if it exists
                if status.stdout:
                    sys.stdout.write(status.stdout)
        except FileNotFoundError:
            sys.stdout.write(f"{command[0]}: command not found\n")

        # Force flush to display output before returning to prompt
        sys.stdout.flush()

if __name__ == "__main__":
    main()