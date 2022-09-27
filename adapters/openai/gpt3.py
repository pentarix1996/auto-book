import openai
from uses_cases.interfaces.itextgenerate import ITextGenerate


class GPT3Client(ITextGenerate):

    def __init__(self,
            organization: str,
            api_key: str,
            model: str = "text-davinci-002",
            max_tokens: int = 1024,
            temperature: float = 0.9,
            top_p: float = 1,
            frequency_penalty:float = 0.1,
            presence_penalty: float = 0.3):
        self.organization = organization
        self.api_key = api_key
        self.model = model
        self.max_tokens = max_tokens
        self.temperature =  temperature
        self.top_p = top_p
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def connect(self):
        openai.api_key = self.api_key
        openai.organization = self.organization

    def generate_text(self, input: str):
        response = openai.Completion.create(
            model=self.model,
            prompt=input,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=self.top_p,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty
        )
        return response["choices"][0]["text"]
