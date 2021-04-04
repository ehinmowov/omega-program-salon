import psycopg2


def create_table():
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cutentry (id serial NOT NULL PRIMARY KEY, employee TEXT, service TEXT, "
                "day TEXT, month TEXT, year TEXT, time TEXT, amount TEXT)")
    conn.commit()
    conn.close()


def add_entry(employee, service, day, month, year, current_time, amount):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO cutentry(employee, service, day, month, year, time, amount) VALUES(%s, %s, %s, %s, %s, %s, %s)",
        (employee, service, day, month, year, current_time, amount))
    conn.commit()
    conn.close()


def view_all():
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cutentry")
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry(employee='%', day='%', month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM cutentry WHERE employee LIKE %s AND day LIKE %s AND month LIKE %s AND year LIKE %s",
                (employee, day, month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_employee_byday(employee='%', day='%', month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cutentry WHERE employee LIKE %s AND day LIKE %s AND month LIKE %s AND year LIKE %s",
                (employee, day, month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_employee_bymonth(employee='%', month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cutentry WHERE employee LIKE %s AND month LIKE %s AND year LIKE %s",
                (employee, month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_employee_byyear(employee='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cutentry WHERE employee LIKE %s AND year LIKE %s",
                (employee, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_all_byday(day='%', month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cutentry WHERE day LIKE %s AND month LIKE %s AND year LIKE %s",
                (day, month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_all_bymonth(month='%', year='%'):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cutentry WHERE month LIKE %s AND year LIKE %s",
                (month, year))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_all_byyear(year):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cutentry WHERE year = %s", (year,))
    rows = cur.fetchall()
    conn.close()
    return rows


def search_entry_employee_byall(employee):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()

    cur.execute("SELECT * FROM cutentry WHERE employee = %s", (employee,))
    rows = cur.fetchall()
    conn.close()
    return rows


def delete_selected(id):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM cutentry WHERE id=%s", (id,))
    conn.commit()
    conn.close()


def update_selected(id, employee, service, amount):
    conn = psycopg2.connect("dbname='dc02u99hklmful' user='suqvydyiaogjhd' "
                            "password='8bffaf921dc769de743c9cf6550970944b0429e45cce1c17a8ddc081c6398aed' "
                            "host='ec2-52-45-73-150.compute-1.amazonaws.com' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE cutentry SET employee=%s, service=%s, amount=%s WHERE id=%s",
                (employee, service, amount, id))
    conn.commit()
    conn.close()


# delete_selected(3)
# view_all()
create_table()
