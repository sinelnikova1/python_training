from model.group import Group


def test_delete_all_group(app):
    old_groups = app.group.get_group_list()
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    app.group.delete_all_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - len(new_groups) == 0
    # каждому элементу списка присваиваем пустое значение (0), т.е. удаляем
    for i in range(len(old_groups)):
        old_groups = []
    assert old_groups == new_groups
