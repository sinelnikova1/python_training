from selenium.webdriver.support.select import Select
from model.contacts import Contacts
import re


class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("firstname")) > 0):
            wd.find_element_by_link_text("add new").click()

    def add_information_of_person(self, contacts):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contacts_form(contacts)
        # submit to send form
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_data(self, field_data, data):
        wd = self.app.wd
        if data is not None:
            wd.find_element_by_name(field_data).click()
            Select(wd.find_element_by_name(field_data)).select_by_visible_text(data)

    def fill_contacts_form(self, contacts):
        wd = self.app.wd
        # fill basic information of person
        self.change_field_value("firstname", contacts.firstname)
        self.change_field_value("middlename", contacts.middlename)
        self.change_field_value("lastname", contacts.lastname)
        self.change_field_value("nickname", contacts.nickname)
        self.change_field_value("title", contacts.title)
        self.change_field_value("company", contacts.company)
        self.change_field_value("address", contacts.address)
        self.change_field_value("home", contacts.home)
        self.change_field_value("mobile", contacts.mobile)
        self.change_field_value("work", contacts.work)
        self.change_field_value("fax", contacts.work)
        self.change_field_value("email", contacts.email)
        self.change_field_value("email2", contacts.email)
        self.change_field_value("email3", contacts.email)
        self.change_field_value("homepage", contacts.email)
        # select date of bday and anniversary day in the form (drop-down list)
        self.change_field_data("bday", contacts.bday)
        self.change_field_data("bmonth", contacts.bmonth)
        self.change_field_value("byear", contacts.byear)
        self.change_field_data("aday", contacts.aday)
        self.change_field_data("amonth", contacts.amonth)
        self.change_field_value("ayear", contacts.ayear)
        # fill secondary information in the form
        self.change_field_value("address2", contacts.address2)
        self.change_field_value("phone2", contacts.phone2)
        self.change_field_value("notes", contacts.notes)

    def select_first_contact(self):
        wd = self.app.wd
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        # находим все элементы с данным именем, и из них выбираем элемент с нужным индексом
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()
        self.contact_cache = None

# тест не работает
#    def delete_all_empty_contacts(self):
 #       wd = self.app.wd
  #      self.app.return_to_home_page()
   #     # select all empty contacts (empty contacts in the top)
    #    checkboxes = wd.find_elements_by_name("selected[]")
     #   for checkbox in checkboxes:
      #      if not checkbox.is_selected():
       #         checkbox.click()
        # submit deletion
        #wd.find_element_by_xpath("//input[@value='Delete']").click()
        #wd.switch_to_alert().accept()
        #self.app.return_to_home_page()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_all_contacts()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()
        self.contact_cache = None

    def select_all_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_element_by_id("MassCB").click()

    def send_all_contacts(self):
        wd = self.app.wd
        self.select_all_contacts()
        # send e-mail (open email client)
        wd.find_element_by_xpath("//input[@value='Send e-Mail']").click()
        self.app.return_to_home_page()

    def send_some_contacts(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_by_index(index)
        # send e-mail (open email client)
        wd.find_element_by_xpath("//input[@value='Send e-Mail']").click()
        self.app.return_to_home_page()

    def add_first_contact_to_group(self):
        self.add_some_contact_to_group(0)
        self.contact_cache = None

    def add_some_contact_to_group(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_by_index(index)
        # submit add to group
        wd.find_element_by_name("add").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def add_all_contacts_to_group(self):
        wd = self.app.wd
        self.open_add_contact_page()
        self.select_all_contacts()
        # submit add to group
        wd.find_element_by_name("add").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_by_index(index)
        # click view details
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()
        wd.find_element_by_name("modifiy").click()
        self.fill_contacts_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_some_contact_from_edit_page(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def add_empty_contact(self, contacts):
        wd = self.app.wd
        self.open_add_contact_page()
        # submit to send form
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    # кешируем вызов списка (чтобы оптимизировать загрузку списка в каждом тесте)
    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                last_name = cells[1].text
                first_name = cells[2].text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = cells[3].text
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contacts(lastname=last_name, firstname=first_name, address=address,
                                                   id=id, all_phones_from_home_page=all_phones,
                                                   all_emails_from_home_page = all_emails))
        # contacts = list, в этот список будет добавляться найденные значения
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contacts(lastname=lastname, firstname=firstname, id=id, home=homephone,
                        work=workphone, mobile=mobilephone, phone2=secondaryphone)

    def get_contacts_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contacts(home=homephone, work=workphone, mobile=mobilephone, phone2=secondaryphone)

    def get_contact_email_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contacts(lastname=lastname, id=id, email=email, email2=email2, email3=email3)


    def get_contact_address_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        address = wd.find_element_by_name("lastname").get_attribute("value")
        return Contacts(address=address)


