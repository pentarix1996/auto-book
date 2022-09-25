from dataclasses import dataclass

@dataclass
class Book:
    title: str
    genre: str
    chapters: int
    text: str
    summary: str = None

    def __str__(self):
        return f"{self.title}\n\n{self.text}"