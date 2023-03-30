# Используем Python в качестве базового образа
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости из requirements.txt в рабочую директорию
COPY requirements.txt /app/

# Устанавливаем зависимости из requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем исходный код Flask в рабочую директорию
COPY order_controll_app/backend /app/backend/

COPY order_controll_app/main.py /app/
