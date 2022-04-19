import os
from pathlib import Path

pc = ['my_project',
      ['settings', ['qeq', 'kkhb'], 'mainapp', 'adminapp', 'authapp'
       ],
      '123',
      ['222', ['111', '321'], '333'
       ]
      ]


def rec(lst):
    dir_ = os.path.abspath(os.curdir)
    print(dir_)
    for i in range(len(lst)):
        if type(lst[i]) is str:
            if not os.path.exists(lst[i]):
                os.mkdir(f'{dir_}/' + lst[i])
        else:
            os.chdir(f'{dir_}/' + lst[i - 1])
            rec(lst[i])
    os.chdir('..')


rec(pc)


# dir_ = os.path.abspath(os.curdir)
# print(dir_)
# for i in range(len(pc)):
#     if type(pc[i]) == str:
#         if not os.path.exists(pc[i]):
#             os.mkdir(f'{dir_}/' + pc[i])
#     else:
#         os.chdir(f'{dir_}/' + pc[i - 1])
#         for j in range(len(pc[i])):
#             if not os.path.exists(pc[i][j]):
#                 os.mkdir(f'{dir_}/' + pc[i - 1] + '/' + pc[i][j])
#         os.chdir('..')
