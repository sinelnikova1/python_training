def test_delete_all_empty_contacts(app):
    app.contacts.delete_all_empty_contacts()
