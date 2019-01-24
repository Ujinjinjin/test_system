#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List, Dict
import json


def convert_single(answer_list: List[str]):
    dict_answers: List[dict] = list()
    for j in answer_list:
        a_body: str = j
        is_correct: bool = False
        if j[0] == '+':
            a_body = j[1:]
            is_correct = True
        dict_answers.append({
            "body": f'{a_body[0].upper()}{a_body[1:]}',
            "is_correct": is_correct
        })
    return dict_answers


def convert_multiple(answer_list: List[str]):
    return convert_single(answer_list)


def convert_sequence(answer_list: List[str]):
    dict_answers: List[dict] = list()
    for body in answer_list:
        a_body: str = body[3:]
        dict_answers.append({
            "body": f'{a_body[0].upper()}{a_body[1:]}',
            "is_correct": False,
            "seq_number": int(body[1])
        })
    return dict_answers


def convert_connection(answer_list: List[str]):
    return list()


convert = {
    'S': convert_single,
    'M': convert_multiple,
    'O': convert_sequence,
    'C': convert_connection,
}


question_types: Dict[str, str] = {
    'S': 'Single',
    'M': 'Multiple',
    'O': 'Sequence',
    'C': 'Connect',
}


if __name__ == '__main__':
    with open('files/test', 'r', encoding='utf8') as f:
        lines: List[str] = f.read().split('\n')

    questions: List[str] = list()
    answers: List[list] = list()

    buff_answers: List[str] = list()

    for line in lines:
        if line[0] != '\t':
            questions.append(line)
            if len(buff_answers) > 0:
                answers.append(buff_answers)
            buff_answers = list()
        else:
            buff_answers.append(line[1:])

    answers.append(buff_answers)

    dictionary = {
        'questions': list()
    }

    for i in range(len(questions)):
        q_type: str = question_types[questions[i][1]]
        dictionary['questions'].append({
            "body": questions[i][3:],
            "type": q_type,
            "answers": convert[questions[i][1]](answers[i]),
            "shuffle": True
        })

    with open('files/new_test.json', 'w', encoding='utf8') as f:
        json.dump(dictionary, f, ensure_ascii=False, indent=4)
