from main import BooksCollector

class TestBooksCollector:

    #добавление одной книги
    def test_add_new_book_one_book(self, collector):
        collector.add_new_book('Голубая книга сказок')
        assert len(collector.books_genre) == 1

    # добавление одной книги дважды
    def test_add_book_twice_error(self, collector):
        collector.add_new_book('Темная башня')
        collector.add_new_book('Темная башня')
        assert len(collector.books_genre) == 1

    #устанавливаем книге "Темная башня" жанр "Фантастика"
    def test_set_book_genre_fantasy(self, collector):
        collector.books_genre['Темная башня'] = None
        collector.set_book_genre('Темная башня', 'Фантастика')
        assert collector.books_genre['Темная башня'] == 'Фантастика'

    # жанр книги "Смешарики" не Ужасы, детективы, мультфильмы или фантастика
    def test_set_book_genre_comedy(self, collector):
        collector.books_genre['Смешарики'] = None
        collector.set_book_genre('Смешарики', 'Мультфильмы')
        assert collector.books_genre['Смешарики'] != 'Ужасы'
        assert collector.books_genre['Смешарики'] != 'Детективы'
        assert collector.books_genre['Смешарики'] != 'Фантастика'
        assert collector.books_genre['Смешарики'] != 'Комедии'

    # жанр книги "Пупа и Лупа" - Мультфильм
    def test_get_genre_added_book(self, collector):
        collector.books_genre['Пупа и Лупа'] = None
        collector.set_book_genre('Пупа и Лупа', 'Мультфильмы')
        collector.get_book_genre('Пупа и Лупа')
        genre = collector.get_book_genre('Пупа и Лупа')
        assert genre == 'Мультфильмы'

    # выводим список книг с жанром Фантастика
    def test_get_books_with_specific_genre_two_books_with_genre_fantasy(self, collector):
        collector.add_new_book('Темная башня')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Темная башня', 'Фантастика')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert (collector.get_books_with_specific_genre('Фантастика') == ['Темная башня', 'Гарри Поттер'])

    # в словаре books_genre все добавленные книги
    def test_get_books_genre_have_all_added_books(self, collector):
        collector.add_new_book('Колобок')
        collector.add_new_book('Коробок')
        actual_genres = collector.get_books_genre()
        assert 'Колобок' in actual_genres
        assert 'Коробок' in actual_genres

    # "Пупа и Лупа" и "Гарри Поттер" подходят для детского чтения
    def test_get_books_for_children_Pupa_and_Potter_for_children(self, collector):
        collector.add_new_book('Пупа и Лупа')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Пупа и Лупа', 'Мультфильмы')
        collector.set_book_genre('Гарри Поттер','Фантастика')
        assert (collector.get_books_for_children() == ['Пупа и Лупа', 'Гарри Поттер'])


    # 3 книги добавлены в избранное
    def test_add_book_in_favorites_add_three_books(self, collector):
         collector.add_new_book('Пупа и Лупа')
         collector.add_new_book('Колобок')
         collector.add_new_book('Коробок')
         collector.add_book_in_favorites('Пупа и Лупа')
         collector.add_book_in_favorites('Колобок')
         collector.add_book_in_favorites('Коробок')
         assert collector.favorites == ['Пупа и Лупа', 'Колобок', 'Коробок']

    #одна книга удалена из избранного
    def test_delete_book_from_favorites_delete_one_book(self, collector):
        collector.add_new_book('Пупа и Лупа')
        collector.add_new_book('Колобок')
        collector.add_new_book('Коробок')
        collector.add_book_in_favorites('Пупа и Лупа')
        collector.add_book_in_favorites('Колобок')
        collector.add_book_in_favorites('Коробок')
        collector.delete_book_from_favorites('Коробок')
        assert collector.favorites == ['Пупа и Лупа', 'Колобок']

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_one_book(self, collector):
        book_title = 'Темная башня'
        collector.add_new_book(book_title)
        collector.add_book_in_favorites('Темная башня')
        favorites = collector.get_list_of_favorites_books()
        assert book_title in favorites

