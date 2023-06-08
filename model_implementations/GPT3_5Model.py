from abstract_model import AbstractModel
import openai

openai.api_key = "<key>"


class GPT35Model(AbstractModel):
    def _send_prompt(self, prompt) -> str:
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
