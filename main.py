import getpass
import os
import shlex
import socket


def main():
    user = getpass.getuser()
    host = socket.gethostname()

    while True:
        try:
            parts = shlex.split(input(f"{user}@{host}:{os.getcwd()}$ "))
        except ValueError:
            print("Ошибка: незакрытая кавычка")
            continue
        except (EOFError, KeyboardInterrupt):
            print()
            break

        if not parts:
            continue

        command = parts[0]
        args = parts[1:]

        if command == "exit":
            break

        if command in {"ls", "cd"}:
            print(f"Команда: {command}, аргументы: {args}")
        else:
            print(f"Ошибка: неизвестная команда '{command}'")


if __name__ == "__main__":
    main()
