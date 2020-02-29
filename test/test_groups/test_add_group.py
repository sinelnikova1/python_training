from model.group import Group


def test_add_group(app, json_groups):
    group = json_groups
    old_groups = app.group.get_group_list()
    app.group.create(group)
    # app.group.count() - в роли хеша функции, предпроверка до выполнения загрузки списка.
    assert len(old_groups) + 1 == app.group.count()
    # если количество соответствует, то можно загрузить новый список
    new_groups = app.group.get_group_list()
    # проверка сравнения старого и нового списка с добавлением элемента
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
