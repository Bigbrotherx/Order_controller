# Используем Python в качестве базового образа
FROM node:18

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем package.json и package-lock.json в рабочую директорию
COPY order_controll_app/frontend/package*.json /app/

# Устанавливаем зависимости
RUN npm install

# Копируем исходный код React в рабочую директорию
COPY order_controll_app/frontend/ /app/

# Собираем статические файлы React
RUN npm run build
