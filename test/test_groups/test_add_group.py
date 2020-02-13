from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #string.punctuation +
    # будет сгенерирована случайная длина случайных символов не превышающая максимальную
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Group(name="", header="", footer="")] + [
    # name = генерируем строку, которая начинается с префикса name + не более 10 случайных символов
    Group(name= random_string("name", 10), header=random_string("header", 20), footer= random_string("footer", 15))
    for i in range(5)
]

# генерируется 8 комбинаций каждого с каждым (полный перебор).
#testdata = [
#    Group(name=name, header=header, footer=footer)
#    for name in ["", random_string("name ", 10)]
#    for header in ["", random_string("header ", 20)]
#    for footer in ["", random_string("footer ", 15)]
#]

@pytest.mark.parametrize("group", testdata, ids=[str(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # app.group.count() - в роли хеша функции, предпроверка до выполнения загрузки списка.
    assert len(old_groups) + 1 == app.group.count()
    # если количество соответствует, то можно загрузить новый список
    new_groups = app.group.get_group_list()
    # проверка сравнения старого и нового списка с добавлением элемента
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
