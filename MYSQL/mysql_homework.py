import mysql.connector as mysql
from mysql.connector import Error

try:
    db = mysql.connect(
        host="localhost",
        user="admin",
        passwd="...",
        database="sm_app"
    )
    print("Connection to MySQL DB successful")

    try:
        # # Create table orders
        with db.cursor() as cursor:
            create_table_query = "CREATE TABLE orders (ord_no INT(5), " \
                                 "purch_amt FLOAT, ord_date DATE, " \
                                 "customer_id INT(4), salesman_id INT(4))"
            cursor.execute(create_table_query)
            print("Table orders created successfully")
        # # Insert data
        with db.cursor() as cursor:
            insert_query = "INSERT INTO orders (ord_no, purch_amt, ord_date," \
                           "customer_id, salesman_id) " \
                           "VALUES (%s, %s, %s, %s, %s)"
            values = [
                (70001, 150.5, '2012-10-5', 3005, 5002),
                (70009, 270.65, '2012-09-10', 3001, 5005),
                (70002, 65.26, '2012-10-05', 3002, 5001),
                (70004, 110.5, '2012-08-17', 3009, 5003),
                (70007, 948.5, '2012-09-10', 3005, 5002),
                (70005, 2400.6, '2012-07-27', 3007, 5001),
                (70008, 5760, '2012-09-10', 3002, 5001),
                (70010, 1983.43, '2012-10-10', 3004, 5006),
                (70003, 2480.4, '2012-10-10', 3009, 5003),
                (70012, 250.45, '2012-06-27', 3008, 5002),
                (70011, 75.29, '2012-08-17', 3003, 5007),
                (70013, 3045.6, '2012-04-25', 3002, 5001)
            ]
            cursor.executemany(insert_query, values)
            db.commit()
            print("Insertion was successfull")
        # Info about 5002
        with db.cursor() as cursor:
            query = "SELECT ord_no, ord_date, purch_amt FROM orders " \
                    "WHERE salesman_id = 5002"
            cursor.execute(query)
            print("Info about salesman 5002:\n", cursor.fetchall())
        # Distinct customers_ids
        with db.cursor() as cursor:
            query = "SELECT DISTINCT customer_id FROM orders"
            cursor.execute(query)
            print("Distinct customers ids:\n", cursor.fetchall())
        # Sorted by data
        with db.cursor() as cursor:
            query = "SELECT ord_date, customer_id, ord_no, purch_amt " \
                    "FROM orders ORDER BY ord_date"
            cursor.execute(query)
            print("Orders sorted be data:\n", cursor.fetchall())
        # Orders 70000-70007
        with db.cursor() as cursor:
            query = "SELECT * FROM orders WHERE ord_no BETWEEN 70000 AND 70007"
            cursor.execute(query)
            print("Orders 70000-70007:\n", cursor.fetchall())
    finally:
        db.close()

except Error as e:
    print(f"The error {e} occurred")
