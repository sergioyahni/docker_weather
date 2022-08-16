FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt
ADD ./app /code/app
CMD ["python", "/code/app/main.py"]
