import os

CURRENT_FILE = os.path.abspath(__file__) # получаем абсолютный путь к текущему файлу
CURRENT_DIRECTORY = os.path.dirname(CURRENT_FILE  ) # получаем абсолютный путь к текущей директории где находится файл с которым работаем
TMP_DIR = os.path.join(CURRENT_DIRECTORY, 'tmp') # делаем склейку пути к текущей директории и папки tmp

if not  os.path.exists(TMP_DIR):
    os.mkdir(TMP_DIR)
