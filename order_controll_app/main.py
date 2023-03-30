import logging

from backend import create_app

app = create_app()
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # Файл хранения логов
    file_log = logging.FileHandler("program.log")
    # Консольный вывод логов
    console_out = logging.StreamHandler()
    logging.basicConfig(
        handlers=(file_log, console_out),
        format="%(asctime)s  %(levelname)s  [%(message)s]",
        level=logging.INFO,
    )
    try:
        # Точка входа во Flask приложение
        app.run(host="0.0.0.0")
    except Exception as error:
        logger.error(f"Program runtime error: {error}")
