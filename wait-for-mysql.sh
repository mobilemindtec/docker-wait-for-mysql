#!/bin/bash

set -e

db_host="$1"
db_port="$2"
db_password="$3"
db_name="$4"
shift 4
cmd="$@"



python /tmp/wait_for_mysql.py -h $db_host -P $db_port -p $db_password -d $db_name


exec $cmd
