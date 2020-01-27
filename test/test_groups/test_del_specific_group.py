from model.group import Group


def test_delete_specific_group(app):
    if app.group.count() < 2:
        while app.group.count() < 2:
            app.group.create(Group(name="test"))
    app.group.delete_specific_group()