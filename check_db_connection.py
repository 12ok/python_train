from fixture.db import DbFixture


db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db.get_groups_with_contact()
    for item in l:
        print(item)
    print(len(l))
finally:
    db.destroy()
