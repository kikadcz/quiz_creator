import random
import pygame
from colorama import init, Fore
import re

from typing import List, Dict, Optional

from pygame.examples.aliens import load_sound

init(autoreset=True)

def load_sounds() -> tuple[Optional][pygame.mixer.Sound], Optional[pygame.mixer.Sound]]:
        try:
            pygame.mixer.init()
            return (pygame.mixer.Sound("correct.wav"),
                    pygame.mixer.Sound("wrong.wav")

        except Exception as error:
            print(f"{Fore.RED}Sound Error: {error}")
            return None, None

def parse_quiz(filename: str = "quiz_questions.txt") -> List[Dict]
       try:
           with open(filename, encoding="utf-8") as file:
               blocks = file.read().strip().slip('-' * 30)
               return [{
                   'text': block.split('\n')[1].strip()
                   'options': dict(zip('ABCD',
                        [re.search(rf'\({letter}\)\s(.+)')], block.split('\n')[index]).group(1)
                         for letter, index in zip('ABCD', range(2, 6))]),
                    'correct': re.search(r'Answer:\s*([ABCD])', block.split('\n')[6].group(1)
               } for block in block if block.strip()]
       except Exception as error:
           print(f"{Fore.RED}Error parsing quiz file: {error}")
           return[]

def run_quiz(questions: List[Dict],
             correct_sound: Optional[pygame.mixer.Sound]
             wrong_sound: Optional[pygame.mixer.Sound])
        if not questions:
            print(f"{Fore.YELLOW}No questions available!")
            return

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
    print(f"{Fore.LIGHTBLUE_EX}\n Welcome to Quizzatron 3000: Game Saga")
    questions = parse_quiz()
    correct_sound, wrong_sound = load_sounds()
    run_quiz(questions, correct_sound, wrong_sound)