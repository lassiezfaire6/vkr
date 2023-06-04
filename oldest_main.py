### NEW MAIN

import pandas as pd  # Модуль pandas необходим для удобной работы с таблицами
import psycopg2  # Модуль psycopg2 необходим для подключения к БД из PostgreSQL
from psycopg2 import Error  # Класс Error позволяет обрабатывать любые ошибки и исключения базы данных.


def sql_queries(database, sql_query, success_msg, autocommit=True, user="postgres", password="root", host="127.0.0.1",
                port="5432"):
    try:
        connection = psycopg2.connect(user=user,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        cursor = connection.cursor()
        connection.autocommit = autocommit
        cursor.execute(sql_query)
        print(success_msg)
        print(cursor.rowcount)
        if cursor.rowcount >= 0:
            return cursor.fetchall()
        else:
            return None
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL:", error)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


sql_queries(database="postgres",
            sql_query="CREATE DATABASE test_db",
            success_msg="База данных успешно создана")

sql_queries(database="test_db",
            sql_query="CREATE TABLE inn (id SERIAL PRIMARY KEY, name VARCHAR(50),  surname VARCHAR(50), inn BIGINT)",
            success_msg="Таблица ИНН успешно создана")

sql_queries(database="test_db",
            sql_query="COPY inn FROM 'D:\inn.csv' DELIMITER ';' CSV HEADER;",
            success_msg="Данные успешно добавлены")

data = sql_queries(database="test_db",
                   sql_query="SELECT * FROM inn",
                   success_msg="Данные успешно получены")

df = pd.DataFrame(data)
print(df)


### OLD MAIN

import pandas as pd  # Модуль pandas необходим для удобной работы с таблицами
import psycopg2  # Модуль psycopg2 необходим для подключения к БД из PostgreSQL
from psycopg2 import Error  # Класс Error позволяет обрабатывать любые ошибки и исключения базы данных.


# Создание базы данных test_db
try:
    # Объект подключения connection создаётся с помощью метода connect()
    connection = psycopg2.connect(user="postgres",
                                  # пароль, который указали при установке PostgreSQL
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="postgres")
    # Класс cursor необходим для выполнения операций с базой данных;
    # объект класса создаётся с помощью метода cursor()
    cursor = connection.cursor()
    # Выполнение немедленно и вне транзакции
    connection.autocommit = True
    # Метод execute() позволяет выполнить любой полученный на вход SQL-запрос
    # Данный запрос создаёт базу данных test_db
    cursor.execute("CREATE DATABASE test_db")
    print("База данных успешно создана")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

# Создание таблицы, содержащей имя, фамилию и ИНН
try:
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test_db")
    cursor = connection.cursor()
    # С помощью SQL-запроса создаём таблицу tin со следующими полями:
    # id (serial; первичный ключ), имя (строковый тип), фамилия (строковый тип), ИНН (bigint)
    cursor.execute("CREATE TABLE tin (id SERIAL PRIMARY KEY, name VARCHAR(50),  surname VARCHAR(50), TIN BIGINT)")
    connection.commit()
    print("Таблица ИНН успешно создана")
    # Помещаем в неё данные из файла _tin.csv, находящегося в корне диска D:
    # Указываем разделитель DELIMITER между столбцами - ';', тип файла - CSV, наличие заголовка HEADER
    cursor.execute("COPY tin FROM 'D:\_tin.csv' DELIMITER ';' CSV HEADER;")
    connection.commit()
    print("Данные успешно добавлены")
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")

try:
    connection = psycopg2.connect(user="postgres",
                                  password="root",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="test_db")
    cursor = connection.cursor()
    # Выберем все данные из таблицы tin
    cursor.execute("SELECT * FROM tin")
    # Поместим их в pandas DataFrame df
    df = pd.DataFrame(cursor.fetchall())
    print("Данные успешно получены")
    print(df)
except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
