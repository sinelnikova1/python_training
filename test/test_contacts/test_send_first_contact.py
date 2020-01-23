def test_send_first_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contacts.send_first_contacts()
    app.session.logout()
