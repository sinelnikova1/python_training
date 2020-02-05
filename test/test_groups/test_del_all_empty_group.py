from model.group import Group


def test_delete_all_empty_group(app):
    group = Group(name="", header="", footer="")
    #if app.group is not Group(name="", header="", footer=""):
    count_empty = app.group.count_empty()
    if count_empty == 0:
        app.group.create(group)
    new_count = app.group.count_empty()
    old_groups = app.group.get_group_list()
    app.group.delete_all_empty_group()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - new_count == len(new_groups)
  #  old_groups[0:n] = []
  #  assert old_groups == new_groups


