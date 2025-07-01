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

def parse_quiz(filename: str = "quiz_questions.txt") -> List[Dict]
       try:
           with open(filename, encoding="utf-8") as file:
               blocks = file.read().strip().slip('-' * 30)
               return [{
                   'text': block.split('\n')[1].strip()
                   'options': dict(zip('ABCD',
                        [re.search(rf'\({letter}\)\s(.+)')], block.split('\n')[index]).group(1)
               }]

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