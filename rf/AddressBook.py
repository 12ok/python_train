import json
import os.path
import re

from fixture.application import Application
from fixture.db import DbFixture
from model.group import Group
from model.contact import Contact


class AddressBook:
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, config="target.json", browser="chrome"):
        self.browser = browser
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", config)
        with open(config_file) as f:
            self.target = json.load(f)

    def init_fixtures(self):
        web_config = self.target['web']
        self.fixture = Application(browser=self.browser, base_url=web_config['baseUrl'])
        self.fixture.session.ensure_login(username=web_config['username'], password=web_config['password'])
        db_config = self.target['db']
        self.dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                                   password=db_config['password'])

    def destroy_fixtures(self):
        self.fixture.destroy()
        self.dbfixture.destroy()

    def get_group_list(self):
        return self.dbfixture.get_group_list()

    def new_group(self, name, header, footer):
        return Group(name=name, header=header, footer=footer)

    def create_group(self, group):
        self.fixture.group.create(group)

    def delete_group(self, group):
        self.fixture.group.delete_group_by_id(group.id)

    def group_list_should_be_equals(self, list1, list2):
        def clear(group):
            return Group(id=group.id, name=re.sub(" +", " ", group.name).strip())

        assert sorted(map(clear, list1), key=Group.id_or_max) == sorted(map(clear, list2), key=Group.id_or_max)

    def get_contact_list(self):
        return self.dbfixture.get_contact_list()

    def new_contact(self, firstname, middlename, lastname):
        return Contact(firstname=firstname, middlename=middlename, lastname=lastname)

    def create_contact(self, contact):
        self.fixture.contact.create(contact)

    def contact_list_should_be_equals(self, list1, list2):
        assert sorted(list1, key=Contact.id_or_max) == sorted(list2, key=Contact.id_or_max)

    def delete_contact(self, contact):
        self.fixture.contact.delete_contact_by_id(contact.id)

    def get_non_empty_contact_list(self):
        if len(self.dbfixture.get_contact_list()) == 0:
            self.fixture.contact.create(Contact(firstname="Name", middlename="Middle", lastname="Surname"))
        return self.dbfixture.get_contact_list()

    def modify_contact(self, random_contact, new_contact):
        self.fixture.contact.modify_contact_by_id(new_contact, random_contact.id)
