from abc import ABC

class TextGenerateI(ABC):
	
    def generate_text(self, input: str):
        raise NotImplementedError()