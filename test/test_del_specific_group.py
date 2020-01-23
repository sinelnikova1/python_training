def test_delete_specific_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete_specific_group()
    app.session.logout()