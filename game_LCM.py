import math
import random


def find_lcm(a, b, c):
    # Функция для нахождения НОК трёх чисел
    lcm_ab = (a * b) // math.gcd(a, b)
    lcm_abc = (lcm_ab * c) // math.gcd(lcm_ab, c)
    return lcm_abc


def brain_lcm():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Find the smallest common multiple of given numbers.")

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

        try:
            user_answer = int(user_answer)
        except ValueError:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    if correct_answers == questions_count:
        print(f"Congratulations, {name}!")


if __name__ == "__main__":
    brain_lcm()