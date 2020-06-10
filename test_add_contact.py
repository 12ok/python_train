# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest


class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def test_add_contact(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//input[@value='Login']").click()
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").send_keys("Oleg")
        wd.find_element_by_name("middlename").send_keys("Petrovich")
        wd.find_element_by_name("lastname").send_keys("Ivanov")
        wd.find_element_by_name("nickname").send_keys("opi")
        wd.find_element_by_name("title").send_keys("Mr")
        wd.find_element_by_name("company").send_keys("The name")
        wd.find_element_by_name("address").send_keys("street 10")
        wd.find_element_by_name("home").send_keys("8121234556")
        wd.find_element_by_name("mobile").send_keys("9112223355")
        wd.find_element_by_name("work").send_keys("8127418523")
        wd.find_element_by_name("fax").send_keys("123")
        wd.find_element_by_name("email").send_keys("mailone@rr.rr")
        wd.find_element_by_name("email2").send_keys("mailtwo@tt.tt")
        wd.find_element_by_name("email3").send_keys("mailthree@yy.yy")
        wd.find_element_by_name("homepage").send_keys("www")
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text("10")
        wd.find_element_by_xpath("//option[@value='10']").click()
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text("April")
        wd.find_element_by_xpath("//option[@value='April']").click()
        wd.find_element_by_name("byear").send_keys("1985")
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text("23")
        wd.find_element_by_css_selector("select[name=\"aday\"] > option[value=\"23\"]").click()
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text("December")
        wd.find_element_by_css_selector("select[name=\"amonth\"] > option[value=\"December\"]").click()
        wd.find_element_by_name("ayear").send_keys("2030")
        wd.find_element_by_name("address2").send_keys("city street")
        wd.find_element_by_name("phone2").send_keys("12")
        wd.find_element_by_name("notes").send_keys("none")
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_link_text("Logout").click()
    
    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
