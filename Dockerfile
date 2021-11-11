FROM python:3.9

WORKDIR /app/second

COPY . .
# RUN mkdir /app/second/staticfiles
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

