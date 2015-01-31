phonebook = {'chris': {'name': 'Chris', 'phone': '555-555-5555'}, 'mg': {'name': 'MG', 'phone': '666-666-6666'}}
#python chooses the order of display that suits it best.
for x in phonebook():
    for y in phonebook[x]:
        print phonebook([x][y])

print "-"*75
print "what do you wanna do?"
print "search"
print "add"
print "edit"
print "remove"
print "exit"

choose = raw_input("I would like to: ")

if choose == "search":
    name = raw_input("Enter name: ").lower()
    print phonebook[name]['name']
    print phonebook[name]['phone']
elif choose == "add":
    add_name = raw_input("Enter name: ")
    add_phone = raw_input("Enter phone: ")
    phonebook.update({add_name:{'name': add_name, 'phone': add_phone }})
    print phonebook
elif choose == "edit":
    edit_choose = raw_input("Enter name: ").lower()
    choice_edit = raw_input("what would you like to edit? Name or Phone or both?: ")
    if choice_edit == "name".lower():
        edit_name = raw_input("Change name to: ")
        phonebook[edit_choose]['name'] = edit_name
        phonebook[edit_name] = phonebook[edit_choose]
        phonebook.pop(edit_choose)
        print phonebook
    elif choice_edit == "phone".lower():
        edit_phone = raw_input("Change phone to: ")
        phonebook[edit_choose]['phone'] = edit_phone
        print phonebook

    else:
        edit_name = raw_input("Change name to: ")
        edit_phone = raw_input("Change phone to: ")
        phonebook[edit_name] = phonebook[edit_choose]
        phonebook.update({edit_name:{'name': edit_name, 'phone': edit_phone}})
        phonebook.pop(edit_choose)

    print phonebook
elif choose == "remove":
    remove_choose = raw_input("enter name to remove: ")
    phonebook.pop(remove_choose)
    print phonebook
else:
    exit()