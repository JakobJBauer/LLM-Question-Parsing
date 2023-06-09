import random

from abstract_model import AbstractModel
from time import sleep
from gpt4_openai import GPT4OpenAI


class GPT4Model(AbstractModel):
    def __init__(self, model_name: str, api_token: str):
        super().__init__(model_name)
        self.__time_waited = 0
        self.__prompt_counter = 0
        self.__model = GPT4OpenAI(token=api_token, model="gpt-4")

    def _send_prompt(self, prompt) -> str:
        if self.__prompt_counter == 25:
            self.__prompt_counter = 0
            sleep(3*60*60 - self.__time_waited)
            self.__time_waited = 0
        time_to_wait = random.randint(15, 3 * 60 * 60 // 35)
        self.__time_waited += time_to_wait
        response = self.__model(prompt)
        sleep(time_to_wait)
        self.__prompt_counter += 1
        return response
