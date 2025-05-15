FROM python:3.12

RUN apt-get update && apt-get install -y curl && \
    rm -f /usr/bin/passwd /usr/bin/login /usr/bin/mount /usr/bin/chfn /usr/bin/chsh /usr/bin/gpasswd /usr/bin/newgrp /usr/bin/umount || true && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m appuser

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip setuptools \
    && pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chown -R appuser:appuser /app

HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 CMD curl -f http://localhost:8000/health || exit 1

USER appuser

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
