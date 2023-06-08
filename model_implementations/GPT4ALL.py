from abstract_model import AbstractModel
from gpt4all import GPT4All as __GPT4All


class GPT4AllModel(AbstractModel):
    def _send_prompt(self, prompt) -> str:
        gptj = __GPT4All("ggml-gpt4all-j-v1.3-groovy")
        messages = [{"role": "user", "content": prompt}]
        response = gptj.chat_completion(messages)
        return response["message"]["content"].strip()
