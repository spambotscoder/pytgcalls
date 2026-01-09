FROM python:3.10-slim

# System deps
RUN apt-get update && apt-get install -y \
    ffmpeg \
    git \
    gcc \
    libffi-dev \
    && apt-get clean

# Workdir
WORKDIR /app

# Copy files
COPY . /app

# Upgrade pip
RUN pip install --upgrade pip

# Install python deps
RUN pip install -r requirements.txt

# Start userbot
CMD ["python3", "mic_userbot.py"]
