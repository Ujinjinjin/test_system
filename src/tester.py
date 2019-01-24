#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import random

from .models import Test, Answer, Settings, Question, QuestionType
from .utils import JsonUtils


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

    @staticmethod
    def __get_right_answer(question: Question) -> str:  # Str имеет легкий поиск по строке (if i in str)
        counter = 0
        result = ""
        if question.type == QuestionType.Single:
            for item in question.answers:
                if item.is_correct:
                    return str(counter + 1)
                counter += 1

        if question.type == QuestionType.Multiple:
            for item in question.answers:
                if item.is_correct:
                    result += str(counter + 1)
                counter += 1
            return result

        if question.type == QuestionType.Sequence:
            result = ""
            current_seq_number = 1

            while result.__len__() < question.answers.__len__():
                current_index = 1
                for item in question.answers:
                    if item.seq_number == current_seq_number:
                        result += str(current_index)
                        current_seq_number += 1
                    current_index += 1
            return result

    def check_answer(self, question: Question, user_answer: int) -> str:
        str_user_answer = str(user_answer)
        if str_user_answer.__len__() > question.answers.__len__():
            raise ValueError
        right_answer = self.__get_right_answer(question)

        if question.type == QuestionType.Single:
            self.count_answer(right_answer == str_user_answer)
            return right_answer

        if question.type == QuestionType.Multiple:
            for char in right_answer:
                if char not in str_user_answer:
                    self.count_answer(False)
                    return right_answer
            self.count_answer(True)
            return right_answer

        if question.type == QuestionType.Sequence:
            self.count_answer(right_answer == str_user_answer)
            return right_answer

        else:
            self.count_answer(False)
            return "Возможно у вопроса неправильный тип"

    def count_answer(self, flag: bool):
        if flag:
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
