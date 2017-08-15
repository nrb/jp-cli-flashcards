from kanamoji import KANAMOJI
import logic


def test_randomize_choices_returns_proper_number():
    choices = logic.randomize_choices(KANAMOJI)
    assert 3 == len(choices)


def test_random_choices_are_defined():
    choices = logic.randomize_choices(KANAMOJI)
    for choice in choices:
        assert choice in KANAMOJI


def test_basic_options():
    choices = [{'romaji': 'ji'}]
    output = logic.format_options(choices)
    assert '0 - ji' == output


def test_two_options():
    choices = [{'romaji': 'ji'},
               {'romaji': 'ke'}]
    output = logic.format_options(choices)
    assert '0 - ji\n1 - ke' == output


def test_three_options():
    choices = [{'romaji': 'ji'},
               {'romaji': 'ke'},
               {'romaji': 'ma'}]
    output = logic.format_options(choices)
    assert '0 - ji\n1 - ke\n2 - ma' == output


def test_game_answer_checking():
    game = logic.FlashCardGame('hiragana', KANAMOJI)
    game.choices = [{'romaji': 'su'}]
    game.answer = {'romaji': 'su'}
    assert game.check_answer(0)


def test_game_answer_bounds_checking():
    game = logic.FlashCardGame('hiragana', KANAMOJI)
    game.choices = [{'romaji': 'su'}]
    game.answer = {'romaji': 'su'}
    assert not game.check_answer(1)
    assert not game.check_answer(-1)


def test_game_randomizes_each_time():
    game = logic.FlashCardGame('hiragana', KANAMOJI)
    game.start_question()
    first_choices = game.choices
    first_answer = game.answer
    game.start_question()

    assert not first_choices == game.choices
    assert not first_answer == game.answer
