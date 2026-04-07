ARG PYTHON_IMAGE_VERSION
FROM python:${PYTHON_IMAGE_VERSION}

WORKDIR /app

COPY /app/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

	
COPY . . 

CMD ["gunicorn", "-b", "0.0.0.0:8000", "app.app:app"]
