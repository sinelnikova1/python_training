def test_send_all_contacts(app):
    app.session.login(username="admin", password="secret")
    app.contacts.send_all_contacts()
    app.session.logout()
