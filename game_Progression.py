import random
import math
from game_Engine import *


def generate_geometric_progression():
    # Генерируем случайные параметры прогрессии
    start = random.randint(1, 5)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)

    # Создаём прогрессию
    progression = [start * (ratio ** i) for i in range(length)]

    # Выбираем случайную позицию для скрытия
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    # Создаём строку с вопросом (со скрытым элементом)
    question_progression = progression.copy()
    question_progression[hidden_index] = '..'
    question_str = ' '.join(map(str, question_progression))

    return question_str, correct_answer


def brain_progression():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!\nWhat number is missing in the progression?")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        question, correct_answer = generate_geometric_progression()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if not check_answer(user_answer, correct_answer, name):
            return
        correct_answers = correct_answers + 1
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    brain_progression()