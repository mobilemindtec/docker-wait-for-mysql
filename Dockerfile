FROM python:2.7
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD wait-for-mysql.sh /tmp/
ADD wait_for_mysql.py /tmp/
RUN pip install -r requirements.txt 
ADD . /code/
