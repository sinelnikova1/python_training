def test_add_first_contact_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contacts.add_first_contact_to_group()
    app.session.logout()
