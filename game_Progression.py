import random
import math


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
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers_needed = 3
    correct_answers = 0

    while correct_answers < correct_answers_needed:
        question, correct_answer = generate_geometric_progression()
        print(f"Question: {question}")
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

    print(f"Congratulations, {name}!")


if __name__ == "__main__":
    brain_progression()