from database import engine

conn = engine.connect()
print("Database Connection Succesfull")
print("Closing Database Connection")

conn.close()