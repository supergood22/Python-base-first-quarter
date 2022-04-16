import sys
import json


if __name__ == "__main__":
    if len(sys.argv) == 2:
        num = int(sys.argv[1])
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            b = json.load(f)
            print(b[num-1])
    elif len(sys.argv) > 2:
        num_1, num_2 = int(sys.argv[1]), int(sys.argv[2])
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            b = json.load(f)
            c = b[num_1-1:num_2]
            print(*c, sep='\n')
    else:
        with open('bakery.csv', 'r', encoding='utf-8') as f:
            b = json.load(f)
            print(*b, sep='\n')
