from model.group import Group


def test_edit_specific_group(app):
    if app.group.count() < 2:
        while app.group.count() < 2:
            app.group.create(Group(name="test"))
    app.group.edit_specific_group(Group(name="update group", header="update header", footer="update footer"))


