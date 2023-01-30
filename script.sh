#!/bin/bash

# Set the URL to check
url="https://api.telegram.org/bot6105342986:AAGvBVv9fnemOxPhMarvIbSZSI--0nYeU1w/setWebHook?url=https://unwanted.ae/api/bot"

# Send a request to the URL and store the response code
response_code=$(curl -s -o /dev/null -w "%{http_code}" "$url")