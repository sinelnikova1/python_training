from selenium.webdriver.support.select import Select
from model.contacts import Contacts


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

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def delete_specific_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select specific contacts with serial number in list (удаление по порядковому номеру в списке)
        wd.find_element_by_xpath("(//input[@name='selected[]'])[2]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

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

    def send_first_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_first_contact()
        # send e-mail (open email client)
        wd.find_element_by_xpath("//input[@value='Send e-Mail']").click()
        self.app.return_to_home_page()

    def add_first_contact_to_group(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_first_contact()
        # submit add to group
        wd.find_element_by_name("add").click()
        self.app.return_to_home_page()

    def add_all_contacts_to_group(self):
        wd = self.app.wd
        self.open_add_contact_page()
        self.select_all_contacts()
        # submit add to group
        wd.find_element_by_name("add").click()
        self.app.return_to_home_page()

    def modify_data_from_details(self, new_contact_data):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_first_contact()
        # click view details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("modifiy").click()
        # fill basic information of person
        self.fill_contacts_form(new_contact_data)
        # update contact
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def delete_first_contact_from_edit_page(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        self.select_first_contact()
        # submit deletion
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.app.return_to_home_page()

    def add_empty_contact(self, contacts):
        wd = self.app.wd
        self.open_add_contact_page()
        # submit to send form
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()

    def count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contacts_list(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            last_name = cells[1].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            # contacts = list, в этот список будет добавляться найденные значения
            contacts.append(Contacts(lastname=last_name, id=id))
        return contacts
