import datetime
import DB.Conn as DB_Conn



def getCurrentCount(_date):

    select_query = f"SELECT * FROM click_count where _date = '{_date}'"

    DB_Conn.cursor.execute(select_query)

    records = DB_Conn.cursor.fetchall()

    if records:
        return records[0][1]
    else:
        return 0

def updateClickCount():

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    current_count = getCurrentCount(current_date)

    new_count = current_count + 1

    if current_count:

        query = f"update click_count set _count =  {new_count} where _date = '{current_date}'"

    else:

        query = f"insert into click_count VALUES ('{current_date}',1)"

    DB_Conn.cursor.execute(query)

    DB_Conn.cursor.close()

    DB_Conn.conn.commit()

    DB_Conn.conn.close()


updateClickCount()