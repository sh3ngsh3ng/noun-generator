import json
import random

with open('nouns.json', 'r') as f:
    data = json.load(f)


def get_items(data, num):
    sublist = random.sample(data, num)
    print('\n'.join(sublist))

get_items(data, 20)
