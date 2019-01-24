#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.utils import Utils
from src.tester import Tester

writeln = Utils.print
read = Utils.input
is_invalid_input = False

if __name__ == '__main__':
    writeln(f'{Utils.get_greeting()}, {Utils.get_display_name()}', v_centered=True, clear=True, buffer=0)
    writeln('Добро пожаловать в систему тестирования по предмету Никитиной.')
    writeln('Для запуска нажмите Enter.', wait=True)

    tester: Tester = Tester('files/test.json')

    while True:
        tester.restart()
        # Start
        for q_num, question in enumerate(tester.test.questions):
            while True:
                writeln(f'Количество верных ответов: {tester.correct_answers}', clear=True)
                writeln(f'Вопрос №{q_num + 1} | {question.type.name}', v_centered=True)
                writeln(f'{question.body}\n')
                correct_answer: str
                # No answers
                if len(question.answers) == 0:
                    writeln('На этот вопрос ответ не найдет. Если вы знаете ответ, свяжитесь с Камилем.')
                    writeln('Для продолжения нажмите Enter', wait=True)
                    continue
                # Print answers
                line_len = max([len(answer.body) for answer in question.answers])
                for a_num, answer in enumerate(question.answers):
                    writeln(f'{a_num + 1}. {answer.body}{" " * (line_len - len(answer.body))}')

                if is_invalid_input:
                    writeln('\n')
                    writeln("Invalid input, try again")
                    writeln('\n')
                else:
                    writeln('\n\n')

                try:
                    user_answer = read('Введите номер варианта ответа: ', int)
                    writeln('\r')

                    correct_answer = tester.check_answer(question, user_answer)

                    writeln(f'Ваш ответ: {user_answer} | Верный ответ {correct_answer}')
                    writeln('Для продолжения нажмите Enter', wait=True)

                except (ValueError, IndexError):
                    is_invalid_input = True
                else:
                    is_invalid_input = False
                    break

        # Results
        writeln(f'Ваш результат:', v_centered=True, clear=True)
        writeln(f'Верных ответов: {tester.correct_answers} | {tester.result}%')
        writeln(f'Неверных ответов: {tester.incorrect_answers} | {100 - tester.result}%')

        if tester.result == 100:
            writeln(f'Птица моя, ты орел...')
        elif tester.result >= 90:
            writeln(f'Птица моя, отличный результат!')
        elif tester.result >= 75:
            writeln(f'Птица моя, неплохой результат.')
        elif tester.result >= 60:
            writeln(f'Птица моя, ты можешь лучше.')
        else:
            writeln(f'Птица моя, ты разочаровываешь меня...')

        writeln('\n')
        writeln('Для продолжения нажмите Enter', wait=True)

        # Restart
        writeln(f'Желаете попробовать еще раз?', v_centered=True, clear=True)
        writeln(f'y/n\n')
        user_answer = read('', str)

        if user_answer == 'n':
            break

    writeln('', clear=True, end='')

