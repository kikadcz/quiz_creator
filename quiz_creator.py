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
        for letter in ['a', 'b', 'c', or 'd']:
            choices[letter] = input("{Fore.CYAN}Choice {letter}: ")

        while True:
            correct_answer = input(Fore.LIGHTMAGENTA_EX + "Correct answer: ").lower()
            if correct_answer in ['a', 'b', 'c', or 'd']:
                break
            print(Fore.RED + "Please enter a, b, c, or d.")
