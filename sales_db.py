import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS sales_table (id serial NOT NULL PRIMARY KEY, product TEXT, pieces TEXT, "
                "day TEXT, month TEXT, year TEXT, time TEXT, amount TEXT)")
    conn.commit()
    conn.close()


def add_entry(product, pieces, day, month, year, current_time, amount):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO sales_table(product, pieces, day, month, year, time, amount) VALUES(%s, %s, %s, %s, %s, %s, %s)",
        (product, pieces, day, month, year, current_time, amount))
    conn.commit()
    conn.close()


def view_all():
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM sales_table")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_product_byday(product='%', day='%', month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_table WHERE product LIKE %s AND day LIKE %s AND month LIKE %s AND year LIKE %s",
                (product, day, month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_product_bymonth(product='%', month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_table WHERE product LIKE %s AND month LIKE %s AND year LIKE %s",
                (product, month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_product_byyear(product='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_table WHERE product LIKE %s AND year LIKE %s",
                (product, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_all_byday(day='%', month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_table WHERE day LIKE %s AND month LIKE %s AND year LIKE %s",
                (day, month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_all_bymonth(month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_table WHERE month LIKE %s AND year LIKE %s",
                (month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_all_byyear(year):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_table WHERE year = %s", (year,))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_product_byall(product):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM sales_table WHERE product = %s", (product,))
    rows = cur.fetchall()
    conn.close()
    return rows



create_table()