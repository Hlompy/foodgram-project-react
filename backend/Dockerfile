FROM python:3.7-slim
WORKDIR /app
RUN python -m pip install --upgrade pip
COPY requirements.txt /app
RUN pip3 install -r ./requirements.txt --no-cache-dir
COPY foodgram/ /app
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000"]