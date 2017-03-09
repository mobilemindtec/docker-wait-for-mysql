import MySQLdb
import time
import sys
import getopt

host = "127.0.0.1"
user = "root"
password = ""
port = 3306
db = "mobilemind_erp"

opts, args = getopt.getopt(sys.argv[1:], 'h:u:p:P:d:')

for opt, arg in opts:
	if opt in ("-h", "--db"):
		host = arg
	elif opt in ("-u", "--user"):
		user = arg
	elif opt in ("-p", "--password"):
		password = arg
	elif opt in ("-P", "--port"):
		port = int(arg)
	elif opt in ("-d", "--db"):
		db = arg

message = """
	\n\n\n
	################################ 
	database connect:
	host = %s
	user = %s
	password = %s
	port = %s
	db = %s
	################################ \n\n\n
""" %  (host, user, password, port, db)

print(message)

while True:
	try:
		conn = MySQLdb.connect(host=host, user=user, passwd=password , port=port)

		while True:
			cursor = conn.cursor()
			cursor.execute("show databases like '" + db + "'")
			result = cursor.fetchone()

			if result and len(result) > 0:
				print("database %s create successful", db)
				break
			else:
				print("database %s not created... waiting...", db)
				time.sleep(1)

			cursor.close()

		conn.close()
		break
	except Exception, e:
		print("MYSQL not responds.. waiting for mysql up: %s" % e)
		time.sleep(1)
	

