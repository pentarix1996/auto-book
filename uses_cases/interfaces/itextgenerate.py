from abc import ABC


class ITextGenerate(ABC):
	
    def generate_text(self, input: str):
        raise NotImplementedError()
