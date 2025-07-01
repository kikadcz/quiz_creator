import random
import pygame
from colorama import init, Fore
import re

from typing import List, Dict, Optional, Tuple

from pygame.examples.aliens import load_sound


init(autoreset=True)

def load_sounds() -> Tuple[Optional[pygame.mixer.Sound], Optional[pygame.mixer.Sound]]:
    try:
            pygame.mixer.init()
            return (
                pygame.mixer.Sound("correct.wav"),
                pygame.mixer.Sound("wrong.wav")
            )
    except Exception as error:
            print(f"{Fore.RED}Sound Error: {error}")
            return None, None


def parse_quiz(filename: str = "quiz_questions.txt") -> List[Dict]:
    try:
        with open(filename, encoding="utf-8") as file:
            blocks = file.read().strip().split('-' * 30)

            parsed_questions = []
            for i, block in enumerate(blocks):
                if not block.strip():
                    continue

                lines = block.strip().split('\n')
                question_line = None
                options = {}

                # Find the "Question:" line and grab the line after it
                for j, line in enumerate(lines):
                    if line.strip().lower().startswith("question:"):
                        if j + 1 < len(lines):
                            question_line = lines[j + 1].strip()
                        break

                if not question_line:
                    print(f"{Fore.YELLOW}Warning: Missing question text in block {i}")
                    continue

                # Extract options using lowercase letters
                for letter in 'abcd':
                    pattern = rf'\({letter}\)\s(.+)'
                    match = re.search(pattern, block, re.IGNORECASE)
                    if match:
                        options[letter.upper()] = match.group(1).strip()
                    else:
                        print(f"{Fore.YELLOW}Warning: Missing option {letter.upper()} in question block {i}")
                        options[letter.upper()] = ""

                # Extract correct answer
                correct_match = re.search(r'Answer:\s*([a-dA-D])', block)
                if not correct_match:
                    print(f"{Fore.YELLOW}Warning: Missing correct answer in question block {i}")
                    continue

                correct_answer = correct_match.group(1).upper()

                parsed_questions.append({
                    'text': question_line,
                    'options': options,
                    'correct': correct_answer
                })

            return parsed_questions

    except FileNotFoundError:
        print(f"{Fore.RED}Error: Quiz file '{filename}' not found")
        return []
    except Exception as error:
        print(f"{Fore.RED}Error parsing quiz file: {error}")
        return []

def run_quiz(questions: List[Dict],
             correct_sound: Optional[pygame.mixer.Sound],
             wrong_sound: Optional[pygame.mixer.Sound]):
    if not questions:
        print(f"{Fore.YELLOW}No questions available!")
        return

    random.shuffle(questions)
    score = 0

    for question_number, question in enumerate(questions, 1):
        print(f"\n{Fore.YELLOW}Question {question_number}: {question['text']}")
        for option_letter, option_text in question['options'].items():
            print(f"({option_letter}) {option_text}")  # ✅ Proper option display

        while True:
            answer = input("Your answer (A/B/C/D): ").upper()
            if answer in 'ABCD':
                break
            print(f"{Fore.RED}Invalid option!")

        if answer == question['correct']:
            print(f"{Fore.GREEN}Correct!")
            if correct_sound:
                correct_sound.play()
            score += 1
        else:
            print(f"{Fore.RED}Wrong! The correct answer was {question['correct']}")
            if wrong_sound:
                wrong_sound.play()

    # ✅ Moved outside loop
    print(f"{Fore.MAGENTA}\nQuiz Finished! Final Score: {score}/{len(questions)}")


if __name__ == "__main__":
    print(f"{Fore.LIGHTBLUE_EX}\n Welcome to Quizzatron 3000: Game Saga")
    questions = parse_quiz()
    correct_sound, wrong_sound = load_sounds()
    run_quiz(questions, correct_sound, wrong_sound)