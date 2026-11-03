from database import create_tables
from admin import Movie
from customer import User, Booking

def get_number(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            
def show_movies(movie):
    movies = movie.get_all_movies()
    if not movies:
        print("No movies available.")
        return
    print("\nID | Title | Genre | Show Time | Seats")
    for m in movies:
        print(m[0], "|", m[1], "|", m[2], "|", m[3], "|", m[4])


def main():
    create_tables()
    movie = Movie()
    user = User()
    booking = Booking()

    while True:
        print("\n===== Movie Ticket Booking =====")
        print("1. Register User")
        print("2. View Movies")
        print("3. Book Ticket")
        print("4. Cancel Booking")
        print("5. View My Bookings")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            user.register_user(name, email)

        elif choice == "2":
            show_movies(movie)

        elif choice == "3":
            email = input("Your email: ")
            u = user.get_user_by_email(email)
            if u is None:
                print("User not found. Please register first.")
                continue
            show_movies(movie)
            movie_id = get_number("Movie ID: ")
            seats = get_number("Number of seats: ")
            booking.book_ticket(u[0], movie_id, seats)

        elif choice == "4":
            booking_id = int(input("Booking ID: "))
            booking.cancel_booking(booking_id)

        elif choice == "5":
            email = input("Your email: ")
            u = user.get_user_by_email(email)
            if u is None:
                print("User not found.")
                continue
            bookings = booking.view_user_bookings(u[0])
            if not bookings:
                print("No bookings yet.")
            for b in bookings:
                print(b)

        elif choice == "6":
            print("Thank you! Bye!")
            break

        else:
            print("Invalid choice. Try again.")


main()

def show_movies(movie):
    movies = movie.get_all_movies()
    if not movies:
        print("No movies available.")
        return
    print("\nID | Title | Genre | Show Time | Seats")
    for m in movies:
        print(m[0], "|", m[1], "|", m[2], "|", m[3], "|", m[4])


def main():
    create_tables()
    movie = Movie()
    user = User()
    booking = Booking()

    while True:
        print("\n===== Movie Ticket Booking =====")
        print("1. Register User")
        print("2. View Movies")
        print("3. Book Ticket")
        print("4. Cancel Booking")
        print("5. View My Bookings")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Name: ")
            email = input("Email: ")
            user.register_user(name, email)

        elif choice == "2":
            show_movies(movie)

        elif choice == "3":
            email = input("Your email: ")
            u = user.get_user_by_email(email)
            if u is None:
                print("User not found. Please register first.")
                continue
            show_movies(movie)
            movie_id = int(input("Movie ID: "))
            seats = int(input("Number of seats: "))
            booking.book_ticket(u[0], movie_id, seats)

        elif choice == "4":
            booking_id = int(input("Booking ID: "))
            booking.cancel_booking(booking_id)

        elif choice == "5":
            email = input("Your email: ")
            u = user.get_user_by_email(email)
            if u is None:
                print("User not found.")
                continue
            bookings = booking.view_user_bookings(u[0])
            if not bookings:
                print("No bookings yet.")
            for b in bookings:
                print(b)

        elif choice == "6":
            print("Thank you! Bye!")
            break

        else:
            print("Invalid choice. Try again.")


main()