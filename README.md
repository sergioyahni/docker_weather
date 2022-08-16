# README
docker_weather is a dockerized application that returns the minimum and maximum temperatures, the sunrise and sunset hours, and a 5-day forecast for a location defined by its latitude and longitude. 
The application sends an email to a selected list of recipients.

## Configurations
Email and password: docker_weather/app/config.py 
Define email, password, and SMTP server: docker_weather/app/main.py
List of recipients: docker_weather/app/main.py 
Personalize email: docker_weather/app/document_creator.py 

## Disclaimer
docker_weather uses an Open Meteo RESTful API. This API is free for open-source development and non-commercial use. The  Open Meteo RESTful API has an Attribution-NonCommercial 4.0 International (CC BY-NC 4.0) license.

For more information and please see the Open Meteo website https://open-meteo.com.
