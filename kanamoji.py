import yaml

f = open('data/kana.yml', 'r', encoding='utf-8')
KANAMOJI = yaml.safe_load(f.read())

seion = list(kanamoji for kanamoji in KANAMOJI if kanamoji['kind'] == 'seion')
dakuon = list(kanamoji for kanamoji in KANAMOJI if kanamoji['kind'] == 'dakuon')
