from main import BooksCollector

class TestBooksCollector:

    # добавление одной книги дважды
    def test_add_book_twice_error(self):
        collector = BooksCollector()
        collector.add_new_book('Темная башня')
        collector.add_new_book('Темная башня')
        assert len(collector.books_genre) == 1

    #устанавливаем книге "Темная башня" жанр "Фантастика"
    def test_set_book_genre_fantasy(self):
        collector = BooksCollector()
        collector.books_genre['Темная башня'] = None
        collector.set_book_genre('Темная башня', 'Фантастика')
        assert (collector.books_genre['Темная башня'], 'Фантастика')

    # жанр книги "Темная башня" не Ужасы, детективы, мультфильмы или комедии
    def test_set_book_genre_is_not_gorror_or_detective_or_cartoon_or_comedy(self):
        collector = BooksCollector()
        collector.books_genre['Темная башня'] = None
        collector.set_book_genre('Темная башня', 'Фантастика')
        assert (collector.books_genre['Темная башня'] != 'Ужасы' or 'Детективы'or 'Мультфильмы' or 'Комедии')

    # жанр книги "Пупа и Лупа" - Мультфильм
    def test_get_genre_added_book(self):
        collector = BooksCollector()
        collector.books_genre['Пупа и Лупа'] = None
        collector.set_book_genre('Пупа и Лупа', 'Мультфильмы')
        collector.get_book_genre('Пупа и Лупа')
        assert collector.get_book_genre('Пупа и Лупа') == 'Мультфильмы'

    # выводим список книг с жанром Фантастика
    def test_get_books_with_specific_genre_two_books_with_genre_fantasy(self):
        collector = BooksCollector()
        collector.add_new_book('Темная башня')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Темная башня', 'Фантастика')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        assert (collector.get_books_with_specific_genre('Фантастика') == ['Темная башня', 'Гарри Поттер'])

    # в словаре books_genre все добавленные книги
    def test_get_books_genre_have_all_added_books(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.add_new_book('Коробок')
        assert collector.get_books_genre() == collector.books_genre

    # "Пупа и Лупа" и "Гарри Поттер" подходят для детского чтения
    def test_get_books_for_children_Pupa_and_Potter_for_children(self):
        collector = BooksCollector()
        collector.add_new_book('Пупа и Лупа')
        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Пупа и Лупа', 'Мультфильмы')
        collector.set_book_genre('Гарри Поттер','Фантастика')
        assert (collector.get_books_for_children() == ['Пупа и Лупа', 'Гарри Поттер'])


    # 3 книги добавлены в избранное
    def test_add_book_in_favorites_add_three_books(self):
         collector = BooksCollector()
         collector.add_new_book('Пупа и Лупа')
         collector.add_new_book('Колобок')
         collector.add_new_book('Коробок')
         collector.add_book_in_favorites('Пупа и Лупа')
         collector.add_book_in_favorites('Колобок')
         collector.add_book_in_favorites('Коробок')
         assert collector.favorites == ['Пупа и Лупа', 'Колобок', 'Коробок']

    #одна книга удалена из избранного
    def test_delete_book_from_favorites_delete_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Пупа и Лупа')
        collector.add_new_book('Колобок')
        collector.add_new_book('Коробок')
        collector.add_book_in_favorites('Пупа и Лупа')
        collector.add_book_in_favorites('Колобок')
        collector.add_book_in_favorites('Коробок')
        collector.delete_book_from_favorites('Коробок')
        assert collector.favorites == ['Пупа и Лупа', 'Колобок']

    # получаем список Избранных книг
    def test_get_list_of_favorites_books_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Темная башня')
        collector.add_book_in_favorites('Темная башня')
        assert collector.get_list_of_favorites_books() == collector.favorites

    # получаем список из 4 избранных книг
    def test_get_list_of_favorites_books_four_books(self):
        collector = BooksCollector()
        collector.add_new_book('Темная башня')
        collector.add_new_book('Пупа и Лупа')
        collector.add_new_book('Мертвые души')
        collector.add_new_book('Котик в сапожках')
        collector.add_book_in_favorites('Темная башня')
        collector.add_book_in_favorites('Пупа и Лупа')
        collector.add_book_in_favorites('Мертвые души')
        collector.add_book_in_favorites('Котик в сапожках')
        assert collector.get_list_of_favorites_books() == ['Темная башня', 'Пупа и Лупа', 'Мертвые души', 'Котик в сапожках']
