from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_first_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    # удаляем только один элемент, т.к. вырезка включает левую границу, но не включает правую,
    # т.е. удаляем первый элемент
    old_groups[0:1] = []
    assert old_groups == new_groups

