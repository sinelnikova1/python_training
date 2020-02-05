from model.group import Group


def test_delete_specific_group(app):
    if app.group.count() < 2:
        while app.group.count() < 2:
            app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.delete_specific_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[1:2] = []
    assert old_groups == new_groups