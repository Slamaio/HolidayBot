#!/bin/bash

mkdir src
cp main.py src/lambda_function.py
cp -R handlers src/handlers
cp *.py src/
pip install --target ./src aiogram beautifulsoup4 requests
cd src
zip -r bot.zip .
cd ..
mv src/bot.zip .
rm -rf src