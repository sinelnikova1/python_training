from model.group import Group


testdata = [
    Group(name="name1", header= "header1", footer="footer1"),
    Group(name="name2", header= "header2", footer="footer2"),
]

# генерируется 8 комбинаций каждого с каждым (полный перебор).
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name ", 10)]
#    for header in ["", random_string("header ", 20)]
#    for footer in ["", random_string("footer ", 15)]
#]

# генерация тестовых данных
#def random_string(prefix, maxlen):
#    symbols = string.ascii_letters + string.digits + string.punctuation
    # будет сгенерирована случайная длина случайных символов не превышающая максимальную
#    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


#testdata = [Group(name="", header="", footer="")] + [
    # name = генерируем строку, которая начинается с префикса name + не более 10 случайных символов
#    Group(name= random_string("name", 10), header=random_string("header", 20), footer= random_string("footer", 15))
#    for i in range(5)
#]
