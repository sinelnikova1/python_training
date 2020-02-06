from model.group import Group

# не работает
#def test_delete_all_empty_group(app):
#    group = Group(name="", header="", footer="")
#    count_empty = app.group.count_empty()
#    if count_empty == 0:
#        app.group.create(group)
#    else:
#        app.group.count_empty()
#    old_groups = app.group.get_group_list()
#    app.group.delete_all_empty_group()
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) - count_empty == len(new_groups)



