import sys
import subprocess

def main():
    while True:
        # Mostrar el prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Leer y dividir el comando
        command = input().split()

        if not command:
            continue  # Si no hay comando, vuelve a solicitar uno

        # Ejecutar el comando
        try:
            status = subprocess.run(command, capture_output=True, text=True)
            if status.returncode != 0:
                # Comando fallido
                sys.stdout.write(f"{command[0]}: command not found\n")
            else:
                # Mostrar la salida del comando
                sys.stdout.write(status.stdout)
        except FileNotFoundError:
            sys.stdout.write(f"{command[0]}: command not found\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()