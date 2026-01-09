FROM python:3.11-slim

WORKDIR /app

RUN apt update && apt install -y \
    ffmpeg \
    git \
    build-essential \
    libopus0 \
    libopus-dev \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python3", "mic_userbot.py"]
