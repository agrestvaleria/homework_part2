import mysql.connector as mysql
from mysql.connector import Error


# Установка соединения с БД
def create_connection(host_name, user_name, user_password):

    my_connection = None

    try:
        my_connection = mysql.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error {e} occurred")
    return my_connection


connection = create_connection("localhost", "admin", "...")


# Строковый запрос о создании базы данных
def create_database(sql_connection, query):

    try:
        with sql_connection.cursor() as cursor:
            cursor.execute(query)
            print("Created successfully")
    except Error as e:
        print(f"The error {e} occurred")


create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)
