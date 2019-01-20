#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random

from models import Test, Answer, Settings
from utils import Utils, JsonUtils


class Tester:
    def __init__(self, filename: str):
        self.__file_name: str = filename
        self.test: Test = JsonUtils.from_json(self.__get_questions(self.filename))
        self.__correct_answers: int = 0
        self.__incorrect_answers: int = 0
        self.shuffle()

    @property
    def correct_answers(self) -> int:
        return self.__correct_answers

    @property
    def filename(self) -> str:
        return self.__file_name

    @property
    def incorrect_answers(self) -> int:
        return self.__incorrect_answers

    @staticmethod
    def __get_questions(filename: str) -> dict:
        with open(filename, 'r', encoding='utf8') as f:
            return json.load(f)

    def count_answer(self, answer: Answer) -> None:
        if answer.is_correct:
            self.__correct_answers += 1
        else:
            self.__incorrect_answers += 1

    def shuffle(self) -> None:
        random.shuffle(self.test.questions)
        settings: Settings = Settings()

        if settings.shuffle_answers:
            for question in self.test.questions:
                random.shuffle(question.answers)

    @property
    def result(self) -> float:
        return int(self.correct_answers / (self.correct_answers + self.incorrect_answers) * 100)

    def restart(self):
        self.__init__(self.filename)
