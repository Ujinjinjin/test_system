#!/usr/bin/env python
# -*- coding: utf-8 -*-
from src.utils import Utils
from src.tester import Tester

writeln = Utils.print
read = Utils.input

if __name__ == '__main__':
    writeln('Добро пожаловать в систему тестирования ТОиИТЭА.', v_centered=True, clear=True, buffer=0)
    writeln('Для запуска нажмите Enter.', wait=True)

    tester: Tester = Tester('files/test.json')
    
    while True:
        tester.restart()
        # Start
        for q_num, question in enumerate(tester.test.questions):
            writeln(f'Количество верных ответов: {tester.correct_answers}', clear=True)
            writeln(f'Вопрос №{q_num + 1}', v_centered=True)
            writeln(f'{question.body}\n')
            correct_answer: int
            # No answers
            if len(question.answers) == 0:
                writeln('На этот вопрос ответ не найдет. Если вы знаете ответ, свяжитесь с Камилем.')
                writeln('Для продолжения нажмите Enter', wait=True)
                continue
            # Print answers
            line_len = max([len(answer.body) for answer in question.answers])
            for a_num, answer in enumerate(question.answers):
                writeln(f'{a_num + 1}. {answer.body}{" " * (line_len - len(answer.body))}')
                if answer.is_correct:
                    correct_answer = a_num + 1

            writeln('\n\n')

            user_answer = read('Введите номер варианта ответа: ', int)
            writeln('\r')
            
            writeln(f'Ваш ответ: {user_answer} | Верный ответ {correct_answer}')
            tester.count_answer(question.answers[user_answer - 1])
            writeln('Для продолжения нажмите Enter', wait=True)

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

