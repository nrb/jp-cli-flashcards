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
