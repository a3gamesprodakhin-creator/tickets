import subprocess
import sys

# Список библиотек для установки
libraries = ["disnake", "requests", "aiosqlite", "openai", "python-dotenv"]

print("Установка библиотек...")

# Функция для установки библиотек через pip
def install_libraries():
    try:
        for library in libraries:
            print(f"Устанавливаю {library}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", library])
        print("\nБиблиотеки были успешно установлены.")
        print("\nНе забудьте создать .env файл на основе .env.example!")
    except subprocess.CalledProcessError:
        print("Произошла ошибка при установке библиотек.")
        sys.exit(1)

if __name__ == "__main__":
    install_libraries()