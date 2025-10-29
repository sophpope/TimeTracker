import mysql.connector
#from config import USER, PASSWORD, HOST, DATABASE

class DatabaseManager:
    # Handles all of the database operations

    def __init__(self, host, user, password, database):
        self.db = mysql.connector.connect(
            host=host,
            user=user,
            password=password, 
            database=database
        )

        self.cursor = self.db.cursor()
        print("Connected to the Database")

    def save_session(self, app_name, info, start, end):
        # Insert session data into the SQL Database
        duration = (end - start).total_seconds()
        sql = """INSERT INTO time_tracked (app_name, info, start, end, duration_seconds)
                VALUES (%s, %s, %s, %s, %s)"""
        self.cursor.execute(sql,(app_name, info, start, end, duration))
        self.db.commit()
        print(f"Saved: {app_name} | {info} | {duration}s")

    def close(self):
        # Close the database connection
        self.cursor.close()
        self.db.close()
        print("Database connection closed")        

    
