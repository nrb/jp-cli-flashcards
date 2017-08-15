import random


def randomize_choices(source):
    """Randomizes 3 choices from within a source data set"""
    choices = []

    for i in range(0, 3):
        picked = random.choice(source)
        if picked in choices:
            picked = random.choice(source)
        choices.append(picked)
    return choices


def format_options(choices):
    """Formats the chosen options for display"""
    output = []
    for i, choice in enumerate(choices):
        output.append('{} - {}'.format(i, choice['romaji']))
    return '\n'.join(output)


class FlashCardGame:
    def __init__(self, characters, collection):
        self.characters = characters
        self.collection = collection
        self.choices = []
        self.answer = None

    def start_question(self):
        self.choices = randomize_choices(self.collection)
        self.answer = random.choice(self.choices)

    def check_answer(self, guess):
        if guess < 0 or guess > len(self.choices) - 1:
            return False
        return self.choices[guess]['romaji'] == self.answer['romaji']
