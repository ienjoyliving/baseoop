# Проектирование классов

## UML-эскиз

```plantuml
@startuml
class Book {
  - isbn: str
  - author: str
  - title: str
  - borrower: str | None
  + is_available(): bool
  - issue_to(reader: str): None
  - return_book(): None
}

class Library {
  - books: dict[str, Book]
  + add_book(book: Book): None
  + issue_book(isbn: str, reader: str): None
  + return_book(isbn: str): None
  + show_books(): list[Book]
  + available_books(): list[Book]
  - find_book(isbn: str): Book
}

Library "1" o-- "*" Book
@enduml
```

## Ответы на вопросы

1 ISBN, автор и название не должны меняться. Это данные, по которым библиотека узнаёт и находит книгу. Состояние и имя читателя могут меняться при выдаче и возврате.

2 в Book, потому что именно книга должна знать, доступна она и кто её взял. library хранит книги и вызывает методы книги, когда выдаёт или принимает её

3 публичные - методы для обычной работы (добавить книгу, выдать, принять возврат и посмотреть списки). find_book лучше оставить внутренним тк это вспомогательный поиск. (если сделать его публичным, другие части программы смогут обращаться к внутренней логике библиотеки и могут неверно обрабатывать отсутствующую книгу)
