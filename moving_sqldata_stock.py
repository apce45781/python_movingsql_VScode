import pymysql
import pyodbc

def main():
    sqlcursor = sqlserver()
    myconn = mysql()
    moving_data(sqlcursor , myconn)

def moving_data(sqlcursor , myconn):
    sqlcursor.execute(
        "SELECT MAX(ID) FROM stock_day"
    )
    quantity = sqlcursor.fetchone()[0]
    for i in range(1 , quantity + 1):
        sqlcursor.execute(
            f"SELECT * FROM stock_day \
            WHERE ID = {i}"
        )
        print(i)
        data = sqlcursor.fetchone()
        mycursor = myconn.cursor()
        mycursor.execute(
            f"INSERT INTO stock_day \
            VALUES({data[0]} , '{data[1]}' , \
                '{data[2]}' , '{data[3]}' , \
                '{data[4]}' , {data[5]} , \
                {data[6]})"
        )
    myconn.commit()

def mysql():
    conn = pymysql.connect(
        host="127.0.0.1",
        user="root",
        password="root_POSSWORD123",
        db="stock"
    )
    return conn

def sqlserver():
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=localhost;"
        "Database=Stock;"
        "Trusted_Connection=yes"
    )
    return conn.cursor()

if __name__ == "__main__":
    main()