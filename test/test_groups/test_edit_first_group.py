from model.group import Group


def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="update group", header="update header", footer="update footer"))
    app.session.logout()

