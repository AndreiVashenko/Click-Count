import datetime
from db.Conn import conn

def getCount(_date):

    query = f"SELECT * FROM click_count where _date = '{_date}'"

    cursor = conn.cursor()

    with cursor:
        cursor.execute(query)
        records = cursor.fetchall()

    if records:
        return records[0][1]
    else:
        return 0

def updateClickCount():

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    current_count = getCount(current_date)

    new_count = + current_count

    if current_count:

        query = f"update click_count set _count =  {new_count} where _date = '{current_date}'"

    else:

        query = f"insert into click_count VALUES ('{current_date}',1)"

    cursor.execute(query)

    conn.commit()


if __name__ == "main":

    cursor = conn.cursor()

    updateClickCount()

    #cursor.close()

    #conn.close()