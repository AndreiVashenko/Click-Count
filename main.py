import uvicorn
import datetime
from db.conn import conn
from fastapi import FastAPI

app = FastAPI()

cursor = conn.cursor()

def getCount(_date):

    query = f"SELECT * FROM click_count where _date = '{_date}'"

    cursor.execute(query)

    records = cursor.fetchall()

    if records:
        return records[0][1]
    else:
        return 0

@app.get("/{date}")
def app_getCount(date):
    return {f"current count for {date} is": getCount(date)}


@app.get("/")
def app_updateClickCount():

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    current_count = getCount(current_date)

    new_count = current_count + 1

    if current_count:

        query = f"update click_count set _count =  {new_count} where _date = '{current_date}'"

    else:

        query = f"insert into click_count VALUES ('{current_date}',1)"

    cursor.execute(query)

    conn.commit()

    return {"today current count is": new_count}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80, log_level="info")

#updateClickCount()

    #cursor.close()

    #conn.close()