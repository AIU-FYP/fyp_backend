FROM python:3.12.3

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:${PORT:-8000}