import mysql.connector as mysql
from Lesson_17 import creds
import os
import dotenv

dotenv.load_dotenv(override=True)

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=creds.host,
    port=creds.port,
    database=creds.database
)


cursor = db.cursor(dictionary=True)
cursor.execute('SELECT * FROM students')
data = cursor.fetchall()
print(data)