from model.group import Group


def test_edit_specific_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_specific_group(Group(name="update group", header="update header", footer="update footer"))
    app.session.logout()

