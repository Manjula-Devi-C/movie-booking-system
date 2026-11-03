from database import conn, cursor


class Movie:
    def add_movie(self, title, genre, show_time, seats):
        cursor.execute(
            "INSERT INTO movies (title, genre, show_time, available_seats) VALUES (?,?,?,?)",
            (title, genre, show_time, seats))
        conn.commit()
        print("Movie added!")

    def get_all_movies(self):
        cursor.execute("SELECT * FROM movies")
        return cursor.fetchall()

    def update_movie(self, movie_id, show_time):
        cursor.execute(
            "UPDATE movies SET show_time=? WHERE movie_id=?",
            (show_time, movie_id))
        conn.commit()
        print("Movie updated!")

    def delete_movie(self, movie_id):
        cursor.execute("DELETE FROM movies WHERE movie_id=?", (movie_id,))
        conn.commit()
        print("Movie deleted!")