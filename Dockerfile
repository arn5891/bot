FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install -r main.py
CMD ["flask", "run", "--host=0.0.0.0"]
