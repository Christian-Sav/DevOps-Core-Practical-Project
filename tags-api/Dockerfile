FROM python:3.9
WORKDIR /tags-api
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]