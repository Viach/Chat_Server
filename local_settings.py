import mysql.connector

# set db parameters
connector = mysql.connector.connect(user='db_user',
                                    password='user_pass',
                                    host='db_host',
                                    database='db_name')
