# docker-wait-for-mysql
Waiting for MySQL Docker


## About

Docker composer Django + MySQL example

#### docker-composer.yml

```
version: '2'
services:
  db:
    image: mysql
    container_name: database.dev
    #command: mysqld --user=root --verbose
    volumes:
      - ./db_import.sql:/tmp/db_import.sql
      - ./db_import.sh:/tmp/db_import.sh
    ports:
      - "3306:3306"
    environment:
      MYSQL_DATABASE: "mydb"
      MYSQL_USER: "adm"
      MYSQL_PASSWORD: "pass"
      MYSQL_ROOT_PASSWORD: "pass"
      MYSQL_ALLOW_EMPTY_PASSWORD: "no"
  web:
    build: .

    volumes:
      - .:/code
    ports:
      - "8000:8000"
    depends_on:
      - "db"
    command: ["/tmp/wait-for-mysql.sh", "db", "3306", "pass", "mydb", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
```

#### Dockerfile

```
FROM python:2.7
ENV PYTHONBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
ADD wait-for-mysql.sh /tmp/
ADD wait_for_mysql.py /tmp/
RUN pip install -r requirements.txt 
ADD . /code/
```

#### requirements.txt

```
django
MySQL-python
```

#### db_import.sh

```
mysql -u root -p$MYSQL_ROOT_PASSWORD < /tmp/dbcreation.sql

```

#### dbcreation.sql

```

use mydb;

-- data import to created database

```

#### Execute

```

sudo docker-compose build
sudo docker-compose up

```

#### Command to import data

```
sudo docker exec database.dev bash /tmp/db_import.sh

```
