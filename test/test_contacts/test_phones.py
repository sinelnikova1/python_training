import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contacts.get_contacts_list()[0]
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contacts.get_contacts_from_view_page(0)
    contact_from_edit_page = app.contacts.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


#очищаем лишние символы
def clear(s):
    re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contacts):
    return "\n".join(filter(lambda x: x != "", # удаляются пустые строки. что не удалилось - склеивается (последний шаг)
                            map(lambda x: clear(x), #удаляются лишние символы)
                                filter(lambda x: x is not None, #выкидываются все пустые элементы
                                       [contacts.home, contacts.work, contacts.mobile, contacts.phone2]))))


