FROM python:3.8

# Activate virtualenv elegantly and visible to all python/pip related commands.
# Follow https://pythonspeed.com/articles/activate-virtualenv-dockerfile/
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN mkdir /code
WORKDIR /code

# Install dependencies:
COPY requirements.txt .
# COPY package.json .

RUN pip install -r requirements.txt
# RUN npm install

COPY . .

RUN python /code/consultorio/manage.py migrate