import sys
import subprocess

def main():
    while True:
        # Mostrar el prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Leer y dividir el comando
        command = input().strip().split()

        # Si el comando está vacío, vuelve al inicio del bucle
        if not command:
            sys.stdout.write("$ ")
            continue

        # Ejecutar el comando y verificar el código de salida
        status = subprocess.run(command, capture_output=True, text=True)
        
        # Si el comando falla (código de salida diferente de 0)
        if status.returncode != 0:
            sys.stdout.write(f"{command[0]}: command not found")
            sys.stdout.write("$ ")
        else:
            # Mostrar la salida del comando si existe
            if status.stdout:
                sys.stdout.write(status.stdout)
                sys.stdout.write("$ ")
            if status.stderr:
                sys.stdout.write(status.stderr)
                sys.stdout.write("$ ")
        
        # Asegurar que la salida se imprima antes de volver al prompt
        sys.stdout.flush()

if __name__ == "__main__":
    main()