FROM python:3-alpine
WORKDIR /app
ENV FLASK_APP hello.py
RUN pip3 install --no-cache-dir requests
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./app/ .
EXPOSE 8080
CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]