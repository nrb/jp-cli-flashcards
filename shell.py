import cmd
import logic
from kanamoji import KANAMOJI


class FlashCardShell(cmd.Cmd):
    intro = 'A basic Japanese CLI flash card tool'
    prompt = 'your guess > '

    def initialize(self):
        self.game = logic.FlashCardGame('hiragana', KANAMOJI)
        self.prep_question()
        self.ask()

    def prep_question(self):
        self.game.start_question()
        self.prompt_char = self.game.answer[self.game.characters]

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
