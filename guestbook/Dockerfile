FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN useradd -m appuser
USER appuser

ENV APP_TITLE="InhaTC DevOps 방명록"
ENV THEME_COLOR="#0054A6"

EXPOSE 5000

CMD ["python", "app.py"]
