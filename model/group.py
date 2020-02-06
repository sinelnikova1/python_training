__author__ = 'sinelnikova anastasia'
from sys import maxsize


class Group:

    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    # определяет как выглядит объект при выводе на консоль, выводим id и name через ":"
    def __repr__(self):
        return "%s:%s" % (self.id, self.name)

    # объеккты находятся физически в разных местах и не равны поэтому, пишем функцию,
    # которая логически сравнивает равны ли элементы
    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(gr):
        if gr.id:
            return int(gr.id)
        else:
            return maxsize