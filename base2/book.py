class BookAlreadyIssuedError(Exception):
    """Книга уже выдана."""


class BookNotIssuedError(Exception):
    """Книга уже доступна."""


class Book:
    _isbn: str
    _author: str
    _title: str
    _is_available: bool

    # при создании книги сохраняем её данные и делаем её доступной
    def __init__(self, isbn: str, author: str, title: str) -> None:
        self._isbn = isbn
        self._author = author
        self._title = title
        self._is_available = True

    # свойства позволяют прочитать данные но не позволяют задать их заново
    @property
    def isbn(self) -> str:
        return self._isbn

    # автор и название будут доступны только для чтения
    @property
    def author(self) -> str:
        return self._author

    @property
    def title(self) -> str:
        return self._title

    # состояние доступности нельзя изменить через свойство
    @property
    def is_available(self) -> bool:
        return self._is_available

    # выдача будет возможна только для доступной книги
    def issue(self) -> None:
        if not self._is_available:
            raise BookAlreadyIssuedError
        self._is_available = False

    # возврат будеь возможен только для выданной книги
    def return_book(self) -> None:
        if self._is_available:
            raise BookNotIssuedError
        self._is_available = True


if __name__ == "__main__":
    # пример выдача возврат
    book = Book("123", "А. Пушкин", "Капитанская дочка")
    book.issue()
    print(book.is_available)  # false
    book.return_book()
    print(book.is_available)  # true

    # проверяем что название нельзя изменить после создания
    try:
        book.title = "Другое название"
    except AttributeError:
        print("Название нельзя изменить")