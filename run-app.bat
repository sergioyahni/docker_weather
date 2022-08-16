ECHO OFF
START docker build -t weather-app .
START docker run weather-app
