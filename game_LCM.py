import math
import random
from game_Engine import check_answer

def find_lcm(a, b, c):
    # Функция для нахождения НОК трёх чисел
    lcm_ab = (a * b) // math.gcd(a, b)
    lcm_abc = (lcm_ab * c) // math.gcd(lcm_ab, c)
    return lcm_abc


def brain_lcm():
    name = input("Welcome to the Brain Games!\nMay I have your name? ")
    print(f"Hello, {name}!\nFind the smallest common multiple of given numbers.")

    correct_answers = 0
    questions_count = 3  # Количество вопросов в игре

    for _ in range(questions_count):
        # Генерируем три случайных числа
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 100)

        correct_answer = find_lcm(num1, num2, num3)

        print(f"Question: {num1} {num2} {num3}")
        user_answer = input("Your answer: ")

        if not check_answer(user_answer, correct_answer, name):
            return
        correct_answers = correct_answers + 1

        print(f"Congratulations, {name}!")

if __name__ == "__main__":
    brain_lcm()