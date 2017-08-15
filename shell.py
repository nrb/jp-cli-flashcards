import cmd
import logic
from kanamoji import KANAMOJI


class FlashCardShell(cmd.Cmd):
    prompt = '> '

    def initialize(self):
        self.script = ''
        self.game = None
        self.get_script()

    def get_script(self):
        print('A basic Japanese CLI flash card tool')
        print('Which script would you like to practice?')
        print('Hiragana or katakana?')

    def set_script(self, arg):
        if arg not in ('hiragana', 'katakana'):
            print('{} was an invalid choice.')
            self.get_script()
        self.script = arg
        self.game = logic.FlashCardGame(self.script, KANAMOJI)
        self.prompt = 'your guess > '
        self.prep_question()
        self.ask()

    def prep_question(self):
        self.game.start_question()
        self.prompt_char = self.game.answer[self.script]

    def ask(self):
        print(self.prompt_char)
        print(logic.format_options(self.game.choices))

    def guess(self, arg):
        value = int(arg)
        print('You guessed {}'.format(value))
        if self.game.check_answer(value):
            print('Correct!')
            self.prep_question()
            self.ask()
        else:
            print('Try again')
            self.ask()

    def default(self, arg):
        if not self.game:
            self.set_script(arg)
        else:
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
