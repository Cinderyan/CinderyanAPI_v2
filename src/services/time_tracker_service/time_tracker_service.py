#歐睿安版權所有
#CinderyanAPT
#time_tracker_service
#
#
#

from src.models.time_tracker.time_tracker import TimeTracker
import database

class TimeTrackerService:
    def add_time_tracker_entry(entry: TimeTracker, target_date):
        conn = database.time_tracker_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO time_tracker(
                date, 
                working_hours, 
                study_hours
            )
            VALUES(?, ?, ?)
            """, (
                target_date, 
                entry.working_hours, 
                entry.study_hours
            ))
        conn.commit()
        cursor.close()
        conn.close()

    def get_time_tracker_entry(target_date):
            conn = database.time_tracker_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM time_tracker WHERE date = ?
            """, (
                target_date,
            ))
            result = cursor.fetchall()
            cursor.close()
            conn.close()
            return result

    def delete_time_tracker_entry(target_id):
            conn = database.time_tracker_connection()
            cursor = conn.cursor()
            cursor.execute("""
                DELETE FROM time_tracker WHERE id = ?
            """, (
                target_id,
            ))
            deleted_row_count = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return deleted_row_count

    def update_time_tracker_entry(new_working_hours, new_study_hours, target_id):
            conn = database.time_tracker_connection()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE time_tracker 
                SET working_hours = ?, study_hours = ? 
                WHERE id = ?
            """, (
                new_working_hours, 
                new_study_hours, 
                target_id
            ))
            updated_row_count = cursor.rowcount
            conn.commit()
            cursor.close()
            conn.close()
            return updated_row_count
