def test_delete_all_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_all_empty_group()
    app.session.logout()