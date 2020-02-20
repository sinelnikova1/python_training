

def test_emails_on_home_page(app):
    contact_from_home_page = app.contacts.get_contacts_list()[0]
    contact_from_edit_page = app.contacts.get_contact_email_from_edit_page(0)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)


def merge_emails_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "",  # удаляются пустые строки. что не удалилось - склеивается (последний шаг)
                                filter(lambda x: x is not None,  #выкидываются все пустые элементы
                                       [contacts.email, contacts.email2, contacts.email3])))



