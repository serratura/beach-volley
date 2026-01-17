# Usa una versione leggera di Python
FROM python:3.10-slim

# Imposta la cartella di lavoro nel container
WORKDIR /app

# Copia i file dei requisiti e installali
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia tutto il resto del progetto (server.py, templates, ecc.)
COPY . .

# Espone la porta del server Tornado
EXPOSE 8888

# Comando per avviare il server
CMD ["python", "server.py"]