import sqlite3
from database import conn, cursor


class User:
    def register_user(self, name, email):
        try:
            cursor.execute(
                "INSERT INTO users (name, email) VALUES (?,?)",
                (name, email))
            conn.commit()
            print("User registered!")
        except sqlite3.IntegrityError:
            print("This email is already registered!")

    def get_user_by_email(self, email):
        cursor.execute("SELECT * FROM users WHERE email=?", (email,))
        return cursor.fetchone()

class Booking:
    def book_ticket(self, user_id, movie_id, seats):
        cursor.execute(
            "SELECT available_seats FROM movies WHERE movie_id=?",
            (movie_id,))
        row = cursor.fetchone()

        if row is None:
            print("Movie not found!")
            return

        if row[0] < seats:
            print("Not enough seats! Only", row[0], "available.")
            return

        cursor.execute(
            "INSERT INTO bookings (user_id, movie_id, seats_booked) VALUES (?,?,?)",
            (user_id, movie_id, seats))
        cursor.execute(
            "UPDATE movies SET available_seats = available_seats - ? WHERE movie_id=?",
            (seats, movie_id))
        conn.commit()
        print("Ticket booked!")

    def cancel_booking(self, booking_id):
        cursor.execute(
            "SELECT movie_id, seats_booked FROM bookings WHERE booking_id=?",
            (booking_id,))
        row = cursor.fetchone()

        if row is None:
            print("Booking not found!")
            return

        cursor.execute(
            "UPDATE movies SET available_seats = available_seats + ? WHERE movie_id=?",
            (row[1], row[0]))
        cursor.execute("DELETE FROM bookings WHERE booking_id=?", (booking_id,))
        conn.commit()
        print("Booking cancelled!")

    def view_user_bookings(self, user_id):
        cursor.execute("""
            SELECT bookings.booking_id, movies.title, movies.show_time,
                   bookings.seats_booked, bookings.booking_time
            FROM bookings
            JOIN movies ON bookings.movie_id = movies.movie_id
            WHERE bookings.user_id=?
        """, (user_id,))
        return cursor.fetchall()