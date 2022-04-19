import os
import random
from pathlib import Path


dir_sort = {}
folder = 'some_data'
# letters = [chr(code) for code in range(ord('a'), ord('z') + 1)]
# for _ in range(100):
#     f_name = ''.join(random.sample(letters, random.randint(5, 10)))
#     f_content = bytes(random.randint(0, 255)
#                       for _ in range(random.randrange(10 ** 3 + 50)))
#     with open(os.path.join(folder, f'{f_name}.bin'), 'wb') as f:
#         f.write(f_content)

small_files_10 = [item.name for item in os.scandir(folder) if item.stat().st_size < 10]
dir_sort.setdefault(10, len(small_files_10))
small_files_10_100 = [item.name for item in os.scandir(folder) if 10 < item.stat().st_size < 100]
dir_sort.setdefault(100, len(small_files_10_100))
small_files_100_1000 = [item.name for item in os.scandir(folder) if 100 < item.stat().st_size < 1000]
dir_sort.setdefault(1000, len(small_files_100_1000))
print(dir_sort)
