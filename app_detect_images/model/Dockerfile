FROM python:3.10-bookworm


WORKDIR /api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "model.api:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]