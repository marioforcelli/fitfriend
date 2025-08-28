FROM python:3.13-alpine


WORKDIR /src


COPY ./requirements.txt /src/requirements.txt
# COPY ./.env /code/.env


RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt


COPY ./src /src/app


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]    
