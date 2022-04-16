import sys
import json


def add_sale_write(cel):
    # a = []
    # json.dump(a, open('bakery.csv', 'a'))

    with open('bakery.csv', 'r', encoding='utf-8') as f:
        b = json.load(f)
    b.append(cel)
    json.dump(b, open('bakery.csv', 'w'))


add_sale_write(sys.argv[1])
