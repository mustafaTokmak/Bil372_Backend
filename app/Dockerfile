# We simply inherit the Python 3 image. This image does
# not particularly care what OS runs underneath
FROM python:3.7.5-buster


#WORKDIR $APP
RUN apt-get update
# Expose the port uWSGI will listen on
RUN apt-get install uwsgi-plugin-python3 -y

# Copy the requirements file in order to install
# Python dependencies
COPY ./requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# We copy the rest of the codebase into the image
#COPY . .
COPY . /


#WORKDIR /
# Finally, we run uWSGI with the ini file we
# created earlier


RUN pwd
ENV HOME /app
WORKDIR /app
RUN pwd
EXPOSE 5000
#CMD ["uwsgi" ,"--ini" ,"./app.ini"]
CMD ["python","app.py"]  