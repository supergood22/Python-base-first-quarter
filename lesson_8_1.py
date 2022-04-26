import re


def email_parse(email):
    res = re.split(r'[@]', email)
    # print(res)
    email_dict = {'username': res[0], 'domain': res[1]}
    if '.' not in res[1]:
        raise ValueError(f"wrong email: {email}")
    print(email_dict)


email_parse('supergood22@mail.ru')
email_parse('supergood22@mailru')
