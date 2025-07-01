import random
import pygame
from colorama import init, Fore
import re

from typing import List, Dict, Optional

init(autoreset=True)

def load_sounds() -> tuple[Optional][pygame.mixer.Sound], Optional[pygame.mixer.Sound]]:
        try:
            pygame.mixer.init()
            return (pygame.mixer.Sound("correct.wav"),
                    pygame.mixer.Sound("wrong.wav")

        except Exception as error:
            print(f"{Fore.RED}Sound Error: {error}")
            return None, None

def get_question_and_choices():
        print("Type 'exit' to quit.")
        question = input(Fore.GREEN + "Enter your quiz question: ")
        if question.lower() == 'exit':
            return None

        choices = {}
        for letter in ['a', 'b', 'c', 'd']:
            choices[letter] = input(f"{Fore.CYAN}Choice {letter}: ")

        while True:
            correct_answer = input(Fore.LIGHTMAGENTA_EX + "Correct answer: ").lower()
            if correct_answer in ['a', 'b', 'c', 'd']:
                break
            print(Fore.RED + "Please enter a, b, c, or d.")

        return {
            'question' : question,
            'choices'  : choices,
            'correct_answer' : correct_answer

        }

def saving_to_file(data, bong_sound):
        filename = "quiz_questions.txt"
        with open(filename, "a", encoding='utf-8') as file:
            file.write(f"\nQuestion:\n{data['question']}\n")
            for letter, choice in data['choices'].items():
                file.write(f"({letter}) {choice}\n")
            file.write(f"\nAnswer: {data['correct_answer']}\n{'-'*30}\n")

        if bong_sound:
            bong_sound.play()

def main():
    print_header()
    bong_sound = init_sound()

    while True:
        data = get_question_and_choices()
        if data is None:
            print(Fore.YELLOW + "Thanks for using Quizzatron 3000!")
            break

        saving_to_file(data, bong_sound)
        print(Fore.GREEN + "Question saved successfully.")


if __name__ == "__main__":
    main()