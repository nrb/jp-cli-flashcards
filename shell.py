import cmd
import logic
from kanamoji import KANAMOJI
import random


class FlashCardShell(cmd.Cmd):
    intro = 'A basic Japanese CLI flash card tool'
    prompt = 'your guess > '

    def initialize(self):
        self.prep_question()
        self.ask()

    def prep_question(self):
        self.choices = logic.randomize_choices(KANAMOJI)
        self.answer = random.choice(self.choices)
        self.prompt_char = self.answer['hiragana']

    def ask(self):
        print(self.prompt_char)
        print(logic.format_options(self.choices))

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
