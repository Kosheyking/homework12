import logging

# Настраиваем логгер с обработчиком и форматировщиком

logger = logging.getLogger("my_logger")
file_handler = logging.FileHandler('my_logger.log')
logger.addHandler(file_handler)
formatter_one = logging.Formatter("%(levelname)s : %(asctime)s : %(message)s")
file_handler.setFormatter(formatter_one)
logger.setLevel(logging.INFO)
