#歐睿安版權所有
#CinderyanAPT
#deadline_service
#
#
#

from src.models.deadline.deadline import Deadline
import database

class DeadlineService:
    def add_deadline(deadline: Deadline):
        conn = database.deadline_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO deadline(
                date,
                title,
                description,
                status
            )
            VALUES(?, ?, ?, ?),
        """, (
            deadline.date,
            deadline.title,
            deadline.description,
            deadline.status
        ))
        conn.commit()
        cursor.close()
        conn.close()

    def get_deadline(target_date):
        conn = database.deadline_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM deadline WHERE date = ?
        """, (
            target_date,
        )) 
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    
    def delete_deadline(target_id):
        conn = database.deadline_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM deadline WHERE id = ?
        """, (
            target_id,
        ))
        deleted_row_count = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return deleted_row_count

    def update_deadlinne(new_status, target_id):
        conn = database.deadline_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE deadline SET status = ? WHERE id = ?
        """, (
            new_status,
            target_id
        ))
        updated_row_count = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated_row_count
