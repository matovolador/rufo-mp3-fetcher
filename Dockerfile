FROM python:3.10


# set environment variables
ENV DEBIAN_FRONTEND noninteractive
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN set -x \
   && apt update \
   && apt upgrade -y

RUN apt install python3.10-dev

RUN apt install ffmpeg

# set work directory
RUN mkdir /app
WORKDIR /app

# copy files
COPY . /app/

RUN chmod +x ./install-extras.sh && chmod +x ./install.sh

RUN ./install-extras.sh

RUN ./install.sh

# install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x ./app.sh

CMD ["./app.sh"]
