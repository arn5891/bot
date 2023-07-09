FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip freeze > requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80/tcp
EXPOSE 80/udp
EXPOSE 443/tcp
EXPOSE 8081/udp
CMD ["python", "main.py", "runserver", "0.0.0.0:8000"]
