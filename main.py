from config import USER, PASSWORD, HOST, DATABASE
from database_manager import DatabaseManager
from tracker import ActivityTracker

if __name__ == "__main__":
    db = DatabaseManager(HOST, USER, PASSWORD, DATABASE)
    tracker = ActivityTracker(db)
    tracker.run(interval=10)