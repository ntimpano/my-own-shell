import sys
import subprocess

def main():
    while True:
        # Mostrar el prompt
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Leer y dividir el comando
        command = input().strip().split()

        # Ejecutar el comando y verificar el código de salida
        status = subprocess.run(command, capture_output=True, text=True)
        
        # Si el comando falla (código de salida diferente de 0)
        if status.returncode != 0:
            sys.stdout.write(f"{command[0]}: command not found\n")
        
        # Asegurar que la salida se imprima antes de volver al prompt
        sys.stdout.flush()

if __name__ == "__main__":
    main()