import pygame
from colorama import init, Fore
import pyfiglet

init(autoreset=True)


def print_header():
        ascii_art = pyfiglet.figlet_format("QUIZZATRON 3000", font="doom", justify="left", width=240)
        print(Fore.RED + ascii_art)

def init_sound():
        pygame.mixer.init()
        try:
            pygame.mixer.music.load("bg_music.mp3")
            pygame.mixer.music.play(-1)

            bong_sound = pygame.mixer.Sound("bong.wav")
            return bong_sound

        except Exception as audio_error:
            print(Fore.RED + f"\nWarning: Sound initialization failed ({str(audio_error)}). "
                                    "Continuing without sound effects. ")

        return None

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