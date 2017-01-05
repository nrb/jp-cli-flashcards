import cmd
from kanamoji import KANAMOJI
import random


class FlashCardShell(cmd.Cmd):
    intro = 'A basic Japanese CLI flash card tool'
    prompt = 'your guess > '

    def initialize(self):
        self.prep_question()
        self.ask()

    def prep_question(self):
        self.choices = self.randomize_choices()
        self.answer = self.choose_correct_answer(self.choices)
        self.prompt_char = self.answer.hirigana

    def randomize_choices(self):
        choices = []

        for i in range(0, 3):
            picked = random.choice(KANAMOJI)
            if picked in choices:
                picked = random.choice(KANAMOJI)
            choices.append(picked)
        return choices

    def choose_correct_answer(self, choices):
        return random.choice(choices)

    def ask(self):
        print(self.prompt_char)
        for i, choice in enumerate(self.choices):
            print('{} - {}'.format(i, choice.romaji))

    def guess(self, arg):
        value = int(arg)
        print('You guessed {}'.format(value))
        if self.choices[value] == self.answer:
            print('Correct!')
            self.prep_question()
            self.ask()
        else:
            print('Try again')
            self.ask()

    def default(self, arg):
        self.guess(arg)

    def do_exit(self, arg):
        print('Bye')
        return True

    def do_quit(self, arg):
        return self.do_exit(arg)


if __name__ == '__main__':
    shell = FlashCardShell()
    shell.initialize()
    shell.cmdloop()
