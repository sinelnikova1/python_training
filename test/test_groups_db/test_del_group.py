from model.group import Group


def test_delete_first_group(app, db):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test"))
    old_groups = db.get_group_list()
    app.group.delete_first_group()
    assert len(old_groups) - 1 == app.group.count()
    new_groups = db.get_group_list()
    # удаляем только один элемент, т.к. вырезка включает левую границу, но не включает правую,
    # т.е. удаляем первый элемент
    old_groups[0:1] = []
    assert old_groups == new_groups


