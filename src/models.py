#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List
import json

__all__ = ('Answer', 'Question', 'Test', 'Settings')


class Answer:
    body: str
    is_correct: bool


class Question:
    body: str
    type: str
    answers: List[Answer]


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
