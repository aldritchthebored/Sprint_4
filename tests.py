from main import BooksCollector

import pytest


class TestBooksCollector:
    book_list = [
        ('Star Wars', 'Фантастика'),
        ('Scream', 'Ужасы')
    ]

    def test_genre_five_genres(self):
        collector = BooksCollector()
        assert collector.genre == ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']

    @pytest.mark.parametrize("invalid_book_name", ["", "A" * 41])
    def test_add_new_book_invalid_name(self, invalid_book_name):
        collector = BooksCollector()
        collector.add_new_book(invalid_book_name)
        assert invalid_book_name not in collector.get_books_genre()

    @pytest.mark.parametrize('book_name, genre', book_list)
    def test_set_book_genre_two_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre()[book_name] == genre

    @pytest.mark.parametrize('book_name, genre', book_list)
    def test_get_book_genre_two_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name, genre', book_list)
    def test_set_book_genre_specific_book_two_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        collector.get_books_with_specific_genre(genre)
        assert book_name in collector.get_books_with_specific_genre(genre)
        assert collector.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize('book_name, genre', book_list)
    def test_get_books_genre_two_books(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_books_genre() == {book_name: genre}

    def test_get_books_for_children_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Star Wars')
        collector.set_book_genre('Star Wars', 'Фантастика')
        assert collector.get_books_for_children() == ['Star Wars']

    books = ['Devil Wears Prada', '1984']

    @pytest.mark.parametrize('book', books)
    def test_add_book_in_favourite_two_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

    @pytest.mark.parametrize('book', books)
    def test_delete_book_in_favourite_two_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites(book)
        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize('book', books)
    def test_get_list_of_favorites_books_two_books(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)
        collector.add_book_in_favorites(book)
        assert collector.get_list_of_favorites_books() == [book]

