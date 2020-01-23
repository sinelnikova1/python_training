def test_delete_specific_contact(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete_specific_contact()
    app.session.logout()
