filename: database.py

# Import necessary packages
import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cur.execute('''CREATE TABLE IF NOT EXISTS moderation_logs (
                            id INTEGER PRIMARY KEY,
                            user_id INTEGER,
                            action TEXT,
                            timestamp TEXT
                            )''')
        self.conn.commit()

    def log_moderation_action(self, user_id, action, timestamp):
        self.cur.execute('''INSERT INTO moderation_logs (user_id, action, timestamp) VALUES (?, ?, ?)''',
                         (user_id, action, timestamp))
        self.conn.commit()

    def get_moderation_logs(self):
        self.cur.execute('''SELECT * FROM moderation_logs''')
        return self.cur.fetchall()

    def close_connection(self):
        self.conn.close()

# Example usage
# db = Database('moderation_logs.db')
# db.log_moderation_action(user_id=123, action='mute', timestamp='2022-01-01 12:00:00')
# logs = db.get_moderation_logs()
# print(logs)

# Make sure to close the connection when done
# db.close_connection()