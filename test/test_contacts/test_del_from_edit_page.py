def test_del_from_edit_page(app):
    app.session.login(username="admin", password="secret")
    app.contacts.delete_first_contact_from_edit_page()
    app.session.logout()
