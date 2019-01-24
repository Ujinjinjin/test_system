#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Union
import json
from enum import Enum

__all__ = ('Answer', 'Question', 'Test', 'Settings', 'SequenceAnswer', 'QuestionType')


class QuestionType(Enum):
    Single = 0
    Multiple = 1
    Sequence = 2


class Answer:
    body: str
    is_correct: bool


class SequenceAnswer(Answer):
    seq_number: int


class Question:
    body: str
    type: QuestionType
    answers: List[Union[Answer, SequenceAnswer]]


class Test:
    questions: List[Question]


class Settings:
    only_test: bool
    shuffle_answers: bool
    allowed_question_types: List[str]

    def __init__(self):
        self.load()

    def load(self):
        with open('files/settings.json', 'r', encoding='utf8') as f:
            settings = json.load(f)
        self.__dict__ = settings
