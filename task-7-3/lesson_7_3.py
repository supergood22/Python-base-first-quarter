import os
from pathlib import Path
import shutil

pc = ['my_project',
      ['settings', ['__init__.py', 'dev.py', 'prod.py'],
       'mainapp', ['__init__.py', 'models.py', 'views.py', 'templates',
                   ['mainapp',
                    ['base.html', 'index.html']
                    ]
                   ],
       'auth-app', ['__init__.py', 'models.py', 'views.py', 'templates',
                    ['authapp',
                     ['base.html', 'index.html']
                     ]
                    ],
       ]
      ]


def rec(lst):
    dir_ = os.path.abspath(os.curdir)
    # print(dir_)
    for i in range(len(lst)):
        if type(lst[i]) is str:
            if '.' in lst[i]:
                open(lst[i], 'a', encoding='utf-8')

            else:
                if not os.path.exists(lst[i]):
                    os.mkdir(f'{dir_}/' + lst[i])
        else:
            os.chdir(f'{dir_}/' + lst[i - 1])
            rec(lst[i])
    os.chdir('..')


rec(pc)
# dir_t = os.path.abspath(os.curdir)
# print(dir_t)
dir_t = r'D:\Python-base-first-quarter\task-7-3\my_project'
if not os.path.exists(f'{dir_t}/templates'):
    os.mkdir(f'{dir_t}/templates')
if not os.path.exists(f'{dir_t}/templates/authapp'):
    os.mkdir(f'{dir_t}/templates/authapp')
if not os.path.exists(f'{dir_t}/templates/mainapp'):
    os.mkdir(f'{dir_t}/templates/mainapp')

shutil.copy2(r'D:\Python-base-first-quarter\task-7-3\my_project\authapp\templates\authapp\base.html',
             r'D:\Python-base-first-quarter\task-7-3\my_project\templates\authapp')
shutil.copy2(r'D:\Python-base-first-quarter\task-7-3\my_project\authapp\templates\authapp\index.html',
             r'D:\Python-base-first-quarter\task-7-3\my_project\templates\authapp')
shutil.rmtree(r'D:\Python-base-first-quarter\task-7-3\my_project\authapp\templates')

shutil.copy2(r'D:\Python-base-first-quarter\task-7-3\my_project\mainapp\templates\mainapp\base.html',
             r'D:\Python-base-first-quarter\task-7-3\my_project\templates\mainapp')
shutil.copy2(r'D:\Python-base-first-quarter\task-7-3\my_project\mainapp\templates\mainapp\index.html',
             r'D:\Python-base-first-quarter\task-7-3\my_project\templates\mainapp')
shutil.rmtree(r'D:\Python-base-first-quarter\task-7-3\my_project\mainapp\templates')
