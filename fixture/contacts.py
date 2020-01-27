from selenium.webdriver.support.select import Select


class ContactsHelper:

    def __init__(self, app):
        self.app = app

    def open_add_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def add_information_of_person(self, contacts):
        wd = self.app.wd
        self.open_add_contact_page()
        self.fill_contacts_form(contacts)
        # submit to send form
        wd.find_element_by_name("submit").click()
        self.app.return_to_home_page()

    def fill_contacts_form(self, contacts):
        wd = self.app.wd
        # fill basic information of person
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contacts.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contacts.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contacts.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contacts.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contacts.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contacts.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contacts.work)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contacts.fax)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contacts.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contacts.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contacts.homepage)
        # select date of bday and anniversary day in the form (drop-down list)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contacts.bday)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contacts.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contacts.byear)
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contacts.aday)
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contacts.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contacts.ayear)
        # fill secondary information in the form
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contacts.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contacts.phone2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contacts.notes)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

    def delete_specific_contact(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select specific contacts with serial number in list (удаление по порядковому номеру в списке)
        wd.find_element_by_xpath("(//input[@name='selected[]'])[2]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

    def delete_all_empty_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select all empty contacts (empty contacts in the top)
        checkboxes = wd.find_elements_by_class_name('group')
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

    def delete_all_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.app.return_to_home_page()

    def send_all_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        # send e-mail (open email client)
        wd.find_element_by_xpath("//input[@value='Send e-Mail']").click()
        self.app.return_to_home_page()

    def send_first_contacts(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select first contacts if contact not empty
        wd.find_element_by_name("selected[]").click()
        # send e-mail (open email client)
        wd.find_element_by_xpath("//input[@value='Send e-Mail']").click()
        self.app.return_to_home_page()

    def add_first_contact_to_group(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select first contacts if contact not empty
        wd.find_element_by_name("selected[]").click()
        # submit add to group
        wd.find_element_by_name("add").click()
        self.app.return_to_home_page()

    def add_all_contacts_to_group(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        # submit add to group
        wd.find_element_by_name("add").click()
        self.app.return_to_home_page()

    def modify_fio_from_details(self, contacts):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select first contacts if contact not empty
        wd.find_element_by_name("selected[]").click()
        # click view details
        wd.find_element_by_xpath("//img[@alt='Details']").click()
        wd.find_element_by_name("modifiy").click()
        # fill basic information of person
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contacts.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contacts.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contacts.lastname)
        # update contact
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def update_email(self, contacts):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select first contacts if contact not empty
        wd.find_element_by_name("selected[]").click()
        # click view details
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill basic information of person
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contacts.email)
        # update contact
        wd.find_element_by_name("update").click()
        self.app.return_to_home_page()

    def delete_first_contact_from_edit_page(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        wd.find_element_by_xpath("(//input[@name='update'])[3]").click()
        self.app.return_to_home_page()