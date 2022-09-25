from uses_cases.interfaces.textgeneratei import TextGenerateI
from models.book import Book

class BookGenerator:

    def __init__(self, engine: TextGenerateI, title: str, genre: str, chapters: int, summary: str = None) -> None:
        self.engine = engine
        self.title = title
        self.genre = genre
        self.chapters = chapters
        self.summary = summary
    
    def generate_book(self) -> Book:
        gpt_input = f"Escríbeme un libro de {self.genre.lower()}. El libro tendrá {self.chapters} capítulos de larga duración, el título del libro es '{self.title}'\n\n"

        if self.summary:
            gpt_input += f"Sinopsis del libro: {self.summary}\n\n"
        
        gpt_input += f"{self.title}\n\n"

        gpt_input += "Capítulo 1:"
        book_text = "Capítulo 1: "

        for _ in range(self.chapters):
            text_generated = self.engine.generate_text(input=gpt_input)
            book_text += text_generated
            gpt_input += text_generated

        book = Book(title=self.title, genre=self.genre, chapters=self.chapters, text=book_text, summary=self.summary)
        return book
    
    def continue_book(self, book: Book) -> Book:
        gpt_input = f"Escríbeme un libro de {book.genre.lower()}. El libro tendrá {book.chapters} capítulos de larga duración, el título del libro es '{book.title}'\n\n"

        if self.summary:
            gpt_input += f"Sinopsis del libro: {self.summary}\n\n"

        book.chapters += 1
        gpt_input += f"{book.title}\n\n"
        gpt_input += f"{book.text}\n\nCapítulo: {book.chapters}:"


        text_generated = self.engine.generate_text(input=gpt_input)
        book.text += text_generated
        return book
