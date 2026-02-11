import os
from dotenv import load_dotenv

# Загружаем переменные окружения из .env файла
load_dotenv()

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

# Проверяем наличие критических переменных
if not settings['TOKEN']:
    print("⚠️ Внимание: DISCORD_TOKEN не установлен в .env файле!")