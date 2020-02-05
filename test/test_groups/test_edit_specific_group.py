from model.group import Group


def test_edit_specific_group(app):
    if app.group.count() < 2:
        while app.group.count() < 2:
            app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    group = Group(name="update group", header="update header", footer="update footer")
    group.id = old_groups[1].id
    app.group.edit_specific_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[1] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



