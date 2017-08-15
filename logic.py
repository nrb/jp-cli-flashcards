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
