#!/bin/bash

# Set the URL to check
url="https://api.telegram.org/bot5959383988:AAH3Nadk4iRp56DNfOPb7uxJMQ6WZhXOIus/setWebHook?url=https://unwanted.ae/api/bot"

# Send a request to the URL and store the response code
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")