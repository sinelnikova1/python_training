def test_add_all_contacts_to_group(app):
    app.session.login(username="admin", password="secret")
    app.contacts.add_all_contacts_to_group()
    app.session.logout()
