# Используем официальный образ Python
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /app

# Сначала копируем зависимости для использования кэша Docker
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Указываем порт, который будет использоваться
EXPOSE 5000

# Переменные окружения для Flask
#ENV FLASK_APP=app.py
#ENV FLASK_ENV=production

# Команда для запуска приложения
CMD ["flask", "run", "--host=0.0.0.0"]
