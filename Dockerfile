FROM python:3.13-alpine


WORKDIR /app


COPY ./requirements.txt ./requirements.txt
# COPY ./.env /code/.env


RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY ./src ./src/


CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]    
