# !/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
import os
import json
from models import Answer, Question, Test, Settings

__all__ = ('JsonUtils', 'Utils',)


class Utils:

    @staticmethod
    def clear_screen() -> None:
        os.system('cls')

    @staticmethod
    def get_terminal_width() -> int:
        columns, lines = shutil.get_terminal_size()
        return columns

    @staticmethod
    def get_terminal_height() -> int:
        columns, lines = shutil.get_terminal_size()
        return lines

    @staticmethod
    def print(text: str, h_centered: bool = True, v_centered: bool = False, buffer: int = 1,
              clear: bool = False, fill_char: str = ' ', wait: bool = False, end: str = '\n') -> None:
        if clear:
            Utils.clear_screen()

        width: int = Utils.get_terminal_width()
        height: int = Utils.get_terminal_height()
        pre_text: str = ''

        if v_centered:
            pre_text = '\n'*((height // 3) - buffer)

        if not h_centered or len(text) > width:
            print(f'{pre_text}{text}', end=end)
            return

        margin: int = (width - len(text)) // 2

        print(f'{pre_text}{margin*fill_char}{text}{margin*fill_char}', end=end)

        if wait:
            input()

    @staticmethod
    def input(text: str, _type: type, h_centered: bool = True, fill_char: str = ' '):
        width: int = Utils.get_terminal_width()

        if not h_centered or len(text) > width:
            return _type(input())

        margin: int = (width - len(text)) // 2

        return _type(input(f'{margin*fill_char}{text}'))


class JsonUtils:

    SIMPLE_TYPES: tuple = (str, int, float, bool)

    @staticmethod
    def from_json(data: dict) -> Test:
        settings: Settings = Settings()
        new_test: Test = Test()
        questions: list = list()
        for question in data['questions']:
            answers: list = list()
            if settings.only_test and question['no_answer']:
                continue
            for answer in question['answers']:
                new_answer: Answer = Answer()
                new_answer.text = answer['text']
                new_answer.is_correct = answer['is_correct']
                answers.append(new_answer)
            new_question: Question = Question()
            new_question.body = question['body']
            new_question.no_answer = question['no_answer']
            new_question.answers = answers
            questions.append(new_question)
        new_test.questions = questions
        return new_test

    @staticmethod
    def to_json(data, indent=4):
        return json.dumps(data, default=lambda o: o.__dict__, sort_keys=True, indent=indent, ensure_ascii=False)

