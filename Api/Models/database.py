import psycopg2
import json

# importing database login credentials
credentials = json.load(open("./Models/dbConfig.json"))

# establishing the connection
db = psycopg2.connect(
   database = credentials["database"], 
   user = credentials["user"], 
   password = credentials["password"], 
   host = credentials["host"], 
   port =  credentials["port"]
)

# creating a cursor
cursor = db.cursor()

if __name__ == "__main__":
   # test database 
   cursor.execute("SELECT userid FROM users WHERE username = 'lilree599'")
   result = cursor.fetchone()
   print(result)