from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="group", header="group #3", footer="ok"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

