from abstract_model import AbstractModel
from gpt4all import GPT4All as __GPT4All


class GPT4AllModel(AbstractModel):
    def _send_prompt(self, prompt) -> str:
        print(f"Sending prompt ...{prompt[:-100]}")
        gptj = __GPT4All("ggml-gpt4all-j-v1.3-groovy")
        messages = [{"role": "user", "content": prompt}]
        response = gptj.chat_completion(messages)
        print(f"Response: {response}")
        return response["message"]["content"].strip()
