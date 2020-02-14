FROM ubuntu
MAINTAINER Giorgia Novelli<giorgia.novelli@gmail.com>

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-dev
RUN apt-get install -y python3-pip
RUN apt-get install -y libpq-dev

# Set the locale
# ENV LANG C.UTF-8
# ENV LC_ALL C.UTF-8

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000
ENTRYPOINT ["python3"]
CMD ["app.py"]