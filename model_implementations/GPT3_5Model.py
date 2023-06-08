from abstract_model import AbstractModel
import openai
from time import sleep

openai.api_key = "<key>"


class GPT35Model(AbstractModel):
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
