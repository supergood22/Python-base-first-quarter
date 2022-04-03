#4. * (вместо задачи 3) Написать функцию thesaurus_adv(),
# принимающую в качестве аргументов строки в формате «Имя Фамилия»
# и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания
# и содержащие записи, в которых фамилия начинается с соответствующей буквы.
# Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }

def thesaurus_adv(*args_adv):
    # args_adv = tuple(sorted(args_adv))
    # print(args_adv)
    dict_name_adv = {}
    for i in args_adv:
        name_sep = i.split()
        # print(name_sep)
        if dict_name_adv.get(name_sep[1][0]) == None:
            dict_name_adv.setdefault(name_sep[1][0], {})
            dict_name_adv.get(name_sep[1][0]).setdefault(name_sep[0][0], [i])
        else:
            if dict_name_adv.get(name_sep[1][0]).get(name_sep[0][0]) == None:
                dict_name_adv.get(name_sep[1][0]).setdefault(name_sep[0][0], [i])
            else:
                dict_name_adv.get(name_sep[1][0]).get(name_sep[0][0]).append(i)

    print(dict_name_adv)
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")

# thesaurus("Иван", "Мария", "Петр", "Илья")