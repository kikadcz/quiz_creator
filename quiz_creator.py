import os
import pygame
from colorama import init, Fore, Style
import pyfiglet

init(autoreset=True)


#def print_header():


def init_sound():
        pygame.mixer.init()
        try:
            pygame.mixer.music.load("bg_music.mp3")
            pygame.mixer.music.play(-1)
            bong_sound = pygame.mixer.sound("bong.mp3")
            return bong_sound

        except Exception as e:
            print(Fore.RED + f"\nWarning: Sound initialization failed ({str(e)}). "
                                    "Continuing without sound effects. ")

        return None

def get_question_and_choices():
        print("Type 'exit' to quit.")
        question = input(Fore.GREEN + "Enter your quiz question: ")
        if question.lower() == 'exit':
            return None

        choices = {}
        for letter in ['a', 'b', 'c', 'd']:
            choices[letter] = input("{Fore.CYAN}Choice {letter}: ")

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


    while True:
        data = get_question_and_choices()
        if data is None:
            print(Fore.YELLOW + "Thanks for using Quizzatron 3000!")
            break

        saving_to_file(data)
        print(Fore.GREEN + "Question saved successfully.")