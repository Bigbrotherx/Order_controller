import logging

from backend import create_app

logging.basicConfig(
    level=logging.DEBUG,
    filename="program.log",
    format="%(asctime)s, %(levelname)s, %(message)s, %(name)s",
)

app = create_app()


if __name__ == "__main__":
    logging.info("Запуск сервера!")
    app.run(debug=True)
