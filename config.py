import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

print("=" * 50)
print("Проверка загрузки переменных из .env:")
print(f"DISCORD_TOKEN установлен: {'ДА' if os.getenv('DISCORD_TOKEN') else 'НЕТ'}")
print(f"QUESTIONS_CHANNEL_ID: {os.getenv('QUESTIONS_CHANNEL_ID')}")
print(f"Тип QUESTIONS_CHANNEL_ID: {type(os.getenv('QUESTIONS_CHANNEL_ID'))}")
print("=" * 50)

settings = {
    'TOKEN': os.getenv('DISCORD_TOKEN', ''),
    'OWNERID': int(os.getenv('OWNERID', '0')),
    'SUPPORTROLEID': int(os.getenv('SUPPORTROLEID', '0')),
    'STAFFROLE': int(os.getenv('STAFFROLE', '0')),
    'DEVELOPER': int(os.getenv('DEVELOPER', '0')),
    'QUESTIONS_CHANNEL_ID': int(os.getenv('QUESTIONS_CHANNEL_ID', '0')),
    'LOG_CHANNEL_ID': int(os.getenv('LOG_CHANNEL_ID', '0')),
    'CATEGORY_ID': int(os.getenv('CATEGORY_ID', '0')),
}

# Выводим все настройки для проверки
print("\nЗагруженные настройки:")
for key, value in settings.items():
    if key == 'TOKEN':
        token_preview = value[:10] + '...' if len(value) > 10 else value
        print(f"{key}: {token_preview}")
    else:
        print(f"{key}: {value}")
print("=" * 50)

# Проверяем наличие критических переменных
if not settings['TOKEN']:
    print("❌ Внимание: DISCORD_TOKEN не установлен в .env файле!")

if settings['QUESTIONS_CHANNEL_ID'] == 0:
    print("❌ Внимание: QUESTIONS_CHANNEL_ID не установлен или равен 0!")
