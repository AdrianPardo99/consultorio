FROM python:3.8

RUN mkdir /code
WORKDIR /code

# Install dependencies:
COPY requirements.txt .
# COPY package.json .

RUN pip install -r requirements.txt
# RUN npm install

COPY . .

RUN python /code/consultorio/manage.py migrate