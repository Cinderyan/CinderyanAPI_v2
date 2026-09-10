#歐睿安版權所有
#CinderyanAPT
#calender
#
#
#

from src.models.calendar_event.calendar_event import CalendarEvent
import database

class CalendarService:
    def add_calendar_event(event: CalendarEvent):
        conn = database.calendar_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO calendar(
                date, 
                title, 
                description, 
                status)
            VALUES(?, ?, ?, ?)
        """, (
            event.date, 
            event.title, 
            event.description, 
            event.status
        ))
        conn.commit()
        cursor.close()
        conn.close()

    def get_calendar_event(target_date):
        conn = database.calendar_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT * FROM calendar WHERE date = ?
        """, (
            target_date,
        ))
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return result

    def delete_calendar_event(target_id):
        conn = database.calendar_connection()
        cursor = conn.cursor()
        cursor.execute("""
            DELETE FROM calendar WHERE id = ?
        """, (
            target_id,
        ))
        deleted_row_count = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return deleted_row_count
    
    def update_calendar_event(new_status, target_id):
        conn = database.calendar_connection()
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE calendar SET status = ? WHERE id = ?
        """, (
            new_status,
            target_id
        ))
        updated_row_count = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated_row_count

