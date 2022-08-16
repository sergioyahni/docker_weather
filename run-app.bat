ECHO OFF
START /wait docker build -t weather-app .
START docker run weather-app
