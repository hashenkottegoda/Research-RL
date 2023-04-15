FROM python:3

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r PPO-IMPL/requirements.txt

CMD ["python", "PPO-IMPL/main.py"]
