from collections import defaultdict
from lxml import html
from pprint import pprint
import requests


def parse_table(japanese_rows, character_map, insert_key, basic_class):
    """Insert the information in the HTML table into the character dict.

    Romaji will be keys, values are a dictionary of either hirigana or
    katakana characters.

    The `insert_key` argument is the specifier for hirigana vs katakana.

    The `basic_class` argument specifies what kind of sound class the kanamoji
    belongs to.
    """
    max_len = len(japanese_rows)
    row = 0
    while row < max_len:
        ascii_row = row + 1

        japanese_cells = japanese_rows[row].getchildren()
        ascii_cells = japanese_rows[ascii_row].getchildren()

        # First column is sound files
        japanese_cells.pop(0)
        ascii_cells.pop(0)

        for japanese, ascii in zip(japanese_cells, ascii_cells):
            if ascii.text == '-':
                continue
            character_map[ascii.text][insert_key] = japanese.text
            character_map[ascii.text]['romaji'] = ascii.text
            character_map[ascii.text]['class'] = basic_class

        # skip to the next japanese row
        row += 2
    return character_map


def trim_dakuon_tables(dakuontable):
    rows = dakuontable.getchildren()
    rows.pop(12)
    rows.pop(7)
    rows.pop(0)
    return rows


URL = 'https://www.coscom.co.jp/hiragana-katakana/kanatable.html'
response = requests.get(URL)

tree = html.fromstring(response.content)

# These are the basic kana symbols
# 0 is hirigana, 2 is katakana SeiOn basic characters
# 1 and 3 are YoOn compound forms.
seiontables = tree.cssselect('table.kanatable')
hirigana_table = seiontables[0]
katakana_table = seiontables[2]

# The voiced consonant tables
# 0 is the g, z, d, b, and p sounds for hirigana
# 1 is hte same but for katakana
# rows 0, 7, 12 are a single td with large images. they need to be cut out.
# this applies to both.
dakuontables = tree.cssselect('table.kanatableright1')
hirigana_dakuon_table = dakuontables[0]
katakana_dakuon_table = dakuontables[1]

character_map = defaultdict(dict)

hirigana_seion_rows = hirigana_table.getchildren()
character_map = parse_table(hirigana_seion_rows, character_map, 'hirigana', 'seion')

hirigana_dakuon_rows = trim_dakuon_tables(hirigana_dakuon_table)
character_map = parse_table(hirigana_dakuon_rows, character_map, 'hirigana', 'dakuon')

katakana_seion_rows = katakana_table.getchildren()
character_map = parse_table(katakana_seion_rows, character_map, 'katakana', 'seion')

katakana_dakuon_rows = trim_dakuon_tables(katakana_dakuon_table)
character_map = parse_table(katakana_dakuon_rows, character_map, 'katakana', 'dakuon')

pprint(dict(character_map))
#import pdb; pdb.set_trace()  # NOQA
