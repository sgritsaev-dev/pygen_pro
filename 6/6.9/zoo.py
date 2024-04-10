from collections import ChainMap
import json
with open('C:/VS code pets/edu/pygen_prof/6/6.9/zoo.json', encoding='utf-8') as zoo_json:
    zoo = json.load(zoo_json)
    chain = ChainMap(*zoo)
    print(sum(chain.values()))