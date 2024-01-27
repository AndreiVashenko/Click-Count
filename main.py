import datetime
import DB.Conn as DB_Conn


def getDateExisting(date):
    SelectQuery = f"SELECT * FROM click_count where _date = '{date}'"
    DB_Conn.cursor.execute(SelectQuery)
    records = DB_Conn.cursor.fetchall()
    return bool(len(records))


_date = datetime.datetime.now().strftime("%Y-%m-%d")

isDateExisted = getDateExisting(_date)


InsertQuery = f"insert into click_count VALUES ('{_date}',1)"

DB_Conn.cursor.execute(InsertQuery)

#cursor.execute('SELECT * FROM click_count LIMIT 10')
#records = cursor.fetchall()

DB_Conn.cursor.close()

DB_Conn.conn.commit()

DB_Conn.conn.close()