class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address

    def __repr__(self):
        return "User {}, email: {}, books read: {}".format(self.name, self.email, self.books)

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return True
        
    def read_book(self, book, rating=None):
        self.books[book] = rating
        
    def get_average_rating(self):
        rating = 0
        for value in self.books.values():
            if value:
                rating += value
        return rating / len(self.books)


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []
        
    def get_title(self):
        return self.title
    
    def get_isbn(self):
        return self.isbn
    
    def set_isbn(self, isbn):
        self.isbn = isbn
        print("The ISBN has been updated")
        
    def add_rating(self, rating):
        if rating >= 0 or rating < 5:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")
            
    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return True

    def get_average_rating(self):
        rating = 0
        for r in self.ratings:
            rating += r
        return rating / len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))
    
class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author
        
    def get_author(self):
        return self.author
    
    def __repr__(self):
        return "{} by {}".format(self.title, self.author)
    
class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level
        
    def get_subject(self):
        return self.subject
    
    def get_level(self):
        return self.level
    
    def __repr__(self):
        return "{}, a {} manual on {}".format(self.title, self.level, self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}
    def create_book(self, title, isbn):
        new_book = Book(title, isbn)
        return new_book
        
    def create_novel(self, title, author, isbn):
        new_fiction = Fiction(title, author, isbn)
        return new_fiction

    def create_non_fiction(self, title, subject, level, isbn):
        new_non_fiction = Non_Fiction(title, subject, level, isbn)
        return new_non_fiction

    def add_book_to_user(self, book, email, rating=None):
        if self.users.get(email):
            self.users[email].read_book(book, rating)
            self.books[book] = self.books.get(book, 0) + 1
            if rating:
                book.add_rating(rating)
        else:
            print("No user with email {}!".format(email))
        
    def add_user(self, name, email, user_books=None):
        self.users.update({email: User(name, email)})
        if user_books:
            for b in user_books:
                self.add_book_to_user(b, email)

    def print_catalog(self):
        for b in self.books.keys():
            print(b)
            
    def print_users(self):
        for u in self.users.values():
            print(u)
            
    def most_read_book(self):
        highest_read = 0
        for book, read in self.books.items():
            if read > highest_read:
                highest_read = read
                most_read = book
            else:
                continue
        return most_read
    def highest_rated_book(self):
        max_rating = 0
        for book in self.books.keys():
            book_rating = book.get_average_rating()
            if book_rating > max_rating:
                rated_book = book
                max_rating = book_rating
            else:
                continue
        return rated_book

    def most_positive_user(self):
        rating = 0
        for user in self.users.values():
            user_rating = user.get_average_rating()
            if user_rating > rating:
                rating = user_rating
                highest_rated_user = user.get_email()
            else:
                continue
        return highest_rated_user
