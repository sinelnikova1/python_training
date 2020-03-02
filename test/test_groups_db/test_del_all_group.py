from model.group import Group


def test_delete_all_group(app, db, json_groups, check_ui):
    old_groups = db.get_group_list()
    group = json_groups
    if len(db.get_group_list()) == 0:
        app.group.create(group)
   #     app.group.create(Group(name="test"))
    app.group.delete_all_group()
    new_groups = db.get_group_list()
    for i in range(len(old_groups)):
        old_groups = []
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

