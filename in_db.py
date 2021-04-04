import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Afro_inventory (id serial NOT NULL PRIMARY KEY, product TEXT, "
                "pieces TEXT, price TEXT)")
    conn.commit()
    conn.close()


def add_entry(product, pieces, price):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO Afro_inventory(product, pieces, price) VALUES(%s, %s, %s)",
        (product, pieces, price))
    conn.commit()
    conn.close()


def view_all():
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Afro_inventory")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry(product=''):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM Afro_inventory WHERE product=%s",
                (product,))
    rows = cur.fetchall()
    conn.close()
    return rows


def update_selected(id, product, pieces, price):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
        "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
        "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE Afro_inventory SET product=%s, pieces=%s, price=%s WHERE id=%s",
                (product, pieces, price, id))
    conn.commit()
    conn.close()


create_table()