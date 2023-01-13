from EstimateRank.Locators import *


class Calculate:
    def __init__(self, driver):
        self.driver = driver

    def select_group(self):
        self.driver.find_element('xpath', group).click()

    def lesson1(self, number):
        self.driver.find_element('name', "lessonGrade[0]").send_keys(number)

    def lesson2(self, number):
        self.driver.find_element('name', "lessonGrade[1]").send_keys(number)

    def lesson3(self, number):
        self.driver.find_element('name', "lessonGrade[2]").send_keys(number)

    def lesson4(self, number):
        self.driver.find_element('name', "lessonGrade[3]").send_keys(number)

    def lesson5(self, number):
        self.driver.find_element('name', "lessonGrade[4]").send_keys(number)

    def lesson6(self, number):
        self.driver.find_element('name', "lessonGrade[5]").send_keys(number)

    def lesson7(self, number):
        self.driver.find_element('name', "lessonGrade[6]").send_keys(number)

    def click_on_calculate_button(self):
        self.driver.find_element('xpath', calculate_btn).click()

    def calculate_eror_massage(self):
        self.driver.find_element('id', calculate_eror).click()

    def calculate_validation(self):
        self.driver.find_element('id', rank_validation).click()
