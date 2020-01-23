def test_delete_all_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete_all_contacts()
    app.session.logout()
