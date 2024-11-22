# tests/test_book.py

import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        """
        Set up a Book object for testing.
        This method is called before each test.
        """
        self.book = Book(
            title="1984",
            author="George Orwell",
            isbn="978-0451524935",
            publication_year=1949,
            copies_available=3,
            genre="Dystopian"
        )

    def test_initialization(self):
        """
        Test that the Book object is initialized correctly.
        """
        self.assertEqual(self.book.title, "1984")
        self.assertEqual(self.book.author, "George Orwell")
        self.assertEqual(self.book.isbn, "978-0451524935")
        self.assertEqual(self.book.publication_year, 1949)
        self.assertEqual(self.book.copies_available, 3)
        self.assertEqual(self.book.genre, "Dystopian")

    def test_is_available_true(self):
        """
        Test that is_available returns True when copies are available.
        """
        self.assertTrue(self.book.is_available())

    def test_is_available_false(self):
        """
        Test that is_available returns False when no copies are available.
        """
        self.book.copies_available = 0
        self.assertFalse(self.book.is_available())

    def test_borrow_book_success(self):
        """
        Test that borrowing a book decreases copies_available by 1.
        """
        initial_copies = self.book.copies_available
        self.book.borrow_book()
        self.assertEqual(self.book.copies_available, initial_copies - 1)

    def test_borrow_book_no_copies(self):
        """
        Test that borrowing a book with no copies available raises ValueError.
        """
        self.book.copies_available = 0
        with self.assertRaises(ValueError) as context:
            self.book.borrow_book()
        self.assertEqual(str(context.exception), "No copies available to borrow.")

    def test_return_book(self):
        """
        Test that returning a book increases copies_available by 1.
        """
        initial_copies = self.book.copies_available
        self.book.return_book()
        self.assertEqual(self.book.copies_available, initial_copies + 1)

    def test_multiple_borrows(self):
        """
        Test borrowing multiple times until no copies are left.
        """
        self.book.borrow_book()
        self.book.borrow_book()
        self.book.borrow_book()
        self.assertEqual(self.book.copies_available, 0)
        with self.assertRaises(ValueError):
            self.book.borrow_book()

    def test_multiple_returns(self):
        """
        Test returning multiple books increases the copies_available correctly.
        """
        self.book.copies_available = 1
        self.book.return_book()
        self.book.return_book()
        self.assertEqual(self.book.copies_available, 3)

    def test_repr(self):
        """
        Test the __repr__ method for correct string representation.
        """
        expected_repr = ("Book(title='1984', author='George Orwell', isbn='978-0451524935', "
                        "publication_year=1949, copies_available=3, genre='Dystopian')")
        self.assertEqual(repr(self.book), expected_repr)

    def test_equality(self):
        """
        Test the __eq__ method for comparing two Book objects.
        """
        another_book = Book(
            title="1984",
            author="George Orwell",
            isbn="978-0451524935",
            publication_year=1949,
            copies_available=3,
            genre="Dystopian"
        )
        different_book = Book(
            title="Animal Farm",
            author="George Orwell",
            isbn="978-0451526342",
            publication_year=1945,
            copies_available=5,
            genre="Political Satire"
        )
        self.assertEqual(self.book, another_book)
        self.assertNotEqual(self.book, different_book)

    def test_genre_attribute(self):
        """
        Test that the genre attribute is set correctly.
        """
        self.assertEqual(self.book.genre, "Dystopian")
        self.book.genre = "Science Fiction"
        self.assertEqual(self.book.genre, "Science Fiction")

if __name__ == '__main__':
    unittest.main()
