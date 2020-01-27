from model.group import Group


def test_edit_specific_group(app):
    app.group.edit_specific_group(Group(name="update group", header="update header", footer="update footer"))


