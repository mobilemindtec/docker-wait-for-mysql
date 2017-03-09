# About

Docker composer with python Django app waiting for MySQL database creation



### Help links

* https://docs.docker.com/compose/django/
* https://docs.docker.com/compose/startup-order/


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

### Create django files

```

sudo docker-compose run web django-admin.py startproject mydjangoapp .

```

### change mydjangoapp/settings.py

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydb',
        'USER': 'root',
        'PASSWORD': 'pass',
        'HOST': 'db',
        'PORT': '3306',        
        'OPTIONS': { 'init_command' : 'SET default_storage_engine=INNODB,character_set_connection=utf8,collation_connection=utf8_unicode_ci' }
    }
}

```

### Run container

```

sudo docker-compose build
sudo docker-compose up

```

### Import data command

```
sudo docker exec database.dev bash /tmp/db_import.sh

```
