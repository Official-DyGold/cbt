import mysql.connector

#connection to DB function
def connectionToDB():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="cbt_database"
        )
        if conn.is_connected():
            return conn
    except mysql.connector.Error as e:
        return e

#fetching all data from DB function
def checkDB(queryCheck, params=None):
    conn = connectionToDB()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute(queryCheck, params)
        rows = cursor.fetchall()
        return rows
    except mysql.connector.Error as e:
        return e
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

#Executing query function (save, delete, update)
def bdQuery(query, reportLabel, params=None):
    conn = connectionToDB()
    if conn is None:
        return e
    
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        conn.commit()
        report = f'{reportLabel} Successfully'
        return report
    except mysql.connector.Error as e:
        return e
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()

#fetching one data from DB function
def fetchDB(queryCheck):
    conn = connectionToDB()
    if conn is None:
        return None
    
    cursor = conn.cursor()
    try:
        cursor.execute(queryCheck)
        rows = cursor.fetchone()
        return rows
    except mysql.connector.Error as e:
        return e
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()