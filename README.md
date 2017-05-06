# Chat_Server
Console chat server (sockets)

Simple chat server and client with logging posts into DB.


You need to create file with your DB connector. File name: local_settings.py
```
import mysql.connector

connector = mysql.connector.connect(user=' ',
                                    password=' ',
                                    host=' ',
                                    database=' ')
```
