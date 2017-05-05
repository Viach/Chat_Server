import hashlib
import uuid
import mysql.connector
import datetime as dt

connector = mysql.connector.connect(user='robot00_bosyi',
                                    password='l3nludjl',
                                    host='91.206.201.198',
                                    database='robot00_bosyi')


def get_hashed_password(password):
    salt = uuid.uuid4().hex
    return hashlib.sha512(salt.encode('utf-8') + password.encode('utf-8')).hexdigest() + ":" + salt


def check_password(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return password == hashlib.sha512(salt.encode('utf-8') + user_password.encode('utf-8')).hexdigest()


def save_post(author, text):
    try:
        cursor = connector.cursor()
        sql_stmt = "INSERT INTO post (AUTHOR, TEXT, CREATED_AT)  VALUES (%s, %s, %s)"
        cursor.execute(sql_stmt, (author.strip(), text.strip(), dt.datetime.now()))
        connector.commit()
        return True
    except:
        return False


def tail_posts():
    try:
        cursor = connector.cursor()
        sql_stmt = "SELECT CREATED_AT, AUTHOR, TEXT  from post ORDER BY CREATED_AT DESC LIMIT 10"
        cursor.execute(sql_stmt)
        posts = cursor.fetchall()
        return posts
    except:
        return False


def check_user(name, password):
    cursor = connector.cursor()
    sql_stmt = "SELECT *  FROM  chat_user WHERE name=%s"
    cursor.execute(sql_stmt, (name,))
    row = cursor.fetchone()
    if row:
        id, name, hashed_password = row
        return check_password(hashed_password, password)
    return False


def create_user(name, password):
    if is_username_used(name):  # False if name is used or GUEST
        return False
    try:
        cursor = connector.cursor()
        sql_stmt = "INSERT INTO chat_user (NAME, PASSWORD)  VALUES (%s, %s)"
        cursor.execute(sql_stmt, (name, get_hashed_password(password)))
        connector.commit()
    except:
        return False
    return True


def is_username_used(name):
    cursor = connector.cursor()
    sql_stmt = "SELECT *  FROM  chat_user WHERE name=%s"
    cursor.execute(sql_stmt, (name,))
    row = cursor.fetchone()
    return True if row or name == 'GUEST' else False
