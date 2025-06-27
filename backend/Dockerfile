# ---- Base image ----
FROM python:3.11-slim AS base

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Working directory
WORKDIR /app

# ---- Install dependencies ----
RUN pip install --upgrade pip
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# ---- Copy application ----
COPY app /app/app

# ---- Runtime ----
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
