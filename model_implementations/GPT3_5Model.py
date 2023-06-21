from abstract_model import AbstractModel
import openai
from time import sleep


class GPT35Model(AbstractModel):
    def __init__(self, model_name: str, token: str, **kwargs):
        super().__init__(model_name, **kwargs)
        openai.api_key = token

    def _send_prompt(self, prompt) -> str:
        sleep(2) # Rate limits by openai
        model = "gpt-3.5-turbo"
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        print(response)
        return response["choices"][0]["message"]["content"]
