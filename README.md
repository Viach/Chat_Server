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

Press /h when you start chat_client.py for help:
```
Help : /h - help | /l -login | /t - show last 10 | /u - show active users | /x - exit 
```
