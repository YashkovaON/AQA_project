import time

from selenium.webdriver import Keys

from locators.elements_page_locators import TextBoxPageLocators
from pages.base_page import BasePage


class TextBoxPage(BasePage):
    locators = TextBoxPageLocators()

    def fill_all_fields(self):
        self.element_is_visible(self.locators.full_name).send_keys('Olga')
        self.element_is_visible(self.locators.email).send_keys('ya@ya.com')
        self.element_is_visible(self.locators.current_address).send_keys('US')
        self.element_is_visible(self.locators.permanent_address).send_keys('USA')
        self.element_is_visible(self.locators.submit).send_keys(Keys.ENTER)#click()