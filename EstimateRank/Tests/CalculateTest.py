import os
from EstimateRank.Pages.Calculate import Calculate
from selenium import webdriver
from time import sleep
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class CalculateTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome_options = Options()
        cls.chrome_options.add_argument("--headless")
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service, chrome_options=cls.chrome_options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test1_valid_import_rank(self):
        self.driver.get("https://student.gozine2.ir/EstimateRank/Calculate")
        calculate = Calculate(driver=self.driver)
        calculate.select_group()
        calculate.lesson1("-7")
        calculate.lesson2("50")
        calculate.lesson3("70")
        calculate.lesson4("90")
        calculate.lesson5("0")
        calculate.lesson6("100")
        calculate.lesson7("1")

        sleep(3)
        calculate.click_on_calculate_button()
        calculate.calculate_validation()

        sleep(3)

    def test2_invalid_leave_blank_first_box(self):
        self.driver.get("https://student.gozine2.ir/EstimateRank/Calculate")
        calculate = Calculate(driver=self.driver)
        calculate.select_group()
        calculate.lesson2("50")
        calculate.lesson3("70")
        calculate.lesson4("90")
        calculate.lesson5("0")
        calculate.lesson6("100")
        calculate.lesson7("1")
        calculate.click_on_calculate_button()
        calculate.calculate_eror_massage()

        sleep(3)

    def test3_invalid_leave_blank(self):
        self.driver.get("https://student.gozine2.ir/EstimateRank/Calculate")
        calculate = Calculate(driver=self.driver)
        calculate.select_group()
        calculate.click_on_calculate_button()
        calculate.calculate_eror_massage()

        sleep(3)

    def test4_invalid_import_mistake_rank(self):
        self.driver.get("https://student.gozine2.ir/EstimateRank/Calculate")
        calculate = Calculate(driver=self.driver)
        calculate.select_group()
        calculate.lesson1("110")
        calculate.click_on_calculate_button()
        calculate.calculate_eror_massage()

        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
