from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        # если уже находимся на этой странице c кнопкой new, то ничего делать не нужно
        # (не нужно заново её открывать)
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # init group creation
        wd.find_element_by_name("new").click()
        self.fill_group_form(group)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()
        # после выполнения метода сбрасываем кеш, т.к. метод вносит изменения
        # (т.е. обновляем его, и последующий вызов метода get_group_list будет в новый кеш записываться)
        self.group_cache = None

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    # метод не используется, удалить?
    def select_first_group(self):
        wd = self.app.wd
        # выбираем первый найденный элемент
        wd.find_element_by_name("selected[]").click()

    def select_group_by_index(self, index):
        wd = self.app.wd
        # находим все элементы с данным именем, и из них выбираем элемент с нужным индексом
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_group(self):
        self.delete_group_by_index(0)
        self.group_cache = None

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.return_to_groups_page()
        # select random group
        self.select_group_by_index(index)
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_all_empty_group(self):
        wd = self.app.wd
        self.return_to_groups_page()
        # select all empty groups (empty groups in the top)
        checkboxes = wd.find_elements_by_class_name('group')
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_all_group(self):
        wd = self.app.wd
        self.return_to_groups_page()
        # select all groups
        checkboxes = wd.find_elements_by_css_selector('.group > input')
        for checkbox in checkboxes:
            if not checkbox.is_selected():
                checkbox.click()
        # submit deletion
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def modify_first_group(self):
        self.modify_group_by_index(0)
        self.group_cache = None

    def modify_group_by_index(self, index, new_group_data):
        wd = self.app.wd
        self.return_to_groups_page()
        self.select_group_by_index(index)
        # open modification form
        wd.find_element_by_name("edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def return_to_groups_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(wd.find_elements_by_name("new")) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

# не работает
   # def count_empty(self):
    #    wd = self.app.wd
   #     self.open_group_page()
    #    for elements in wd.find_elements_by_class_name ("group").value_of_css_property("Selected ( )"):
    #        checkboxes = elements.checkboxes
     #       if not elements.is_selected():
     #           elements.click()
#        return len(checkboxes)

    # кешируем вызов списка (чтобы оптимизировать загрузку списка в каждом тесте)
    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector("span.group"):
                text = element.text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.group_cache.append(Group(name = text, id = id))
        # возвращаем не сам кеш, т.к. после тестов он может измениться, а копию кеша, и с ним работать
        return list(self.group_cache) #list в данном случае и есть копия кеша (кеш записывается в список)


