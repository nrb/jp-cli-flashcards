import yaml

f = open('data/kana.yml', 'r', encoding='utf-8')
KANAMOJI = yaml.safe_load(f.read())

seion = list(kana for kana in KANAMOJI if kana['kind'] == 'seion')
dakuon = list(kana for kana in KANAMOJI if kana['kind'] == 'dakuon')
