from adapters.openai.gpt3 import GPT3Client
from adapters.bookgenerator import BookGenerator
from models.book import Book
from configuration.properties import ORGANIZATION, API_KEY, TITLE, CHAPTERS, GENRE, SUMMARY


gpt3 = GPT3Client(organization=ORGANIZATION, api_key=API_KEY)
gpt3.connect()
book_generator = BookGenerator(engine=gpt3, title=TITLE, chapters=CHAPTERS, genre=GENRE, summary=SUMMARY)
book: Book = book_generator.generate_book()


print(f"{book}\n")

while True:
    result: str = input("¿Desea continuar la historia (por defecto N)? (Y/N) > ").lower() or "n"

    while result not in ["y", "n", "yes", "no"]:
        result = input("Valores permitidos (Y/N) ¿Desea continuar la historia (por defecto N)? (Y/N) > ") or "n"
    
    if result in ["n", "no"]:
        break
    book = book_generator.continue_book(book)
    print(f"\n{book}")

print(f"\n{book}")