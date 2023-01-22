from Login.Pages.Login import Login
from selenium import webdriver
from time import sleep
from Login.Pages.MainPage import MainPage
import unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


class LoginTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.chrome_options = Options()
        cls.chrome_options.add_argument("--headless")
        cls.service = Service(executable_path=ChromeDriverManager().install())
        cls.driver = webdriver.Chrome(service=cls.service, chrome_options=cls.chrome_options)
        cls.driver.implicitly_wait(3)
        cls.driver.maximize_window()

    def test1_valid_login(self):
        self.driver.get("https://app.gozine2.ir/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        main_page = MainPage(driver=self.driver)

        login.enter_username("7418700")
        login.enter_password("0020421729")
        login.click_on_login_button()
        main_page.check_main_page()

        sleep(3)

    def test2_invalid_login(self):
        self.driver.get("https://app.gozine2.ir/Login?returnUrl=%2F")
        login = Login(driver=self.driver)

        login.enter_username("0000")
        login.enter_password("0000")
        login.click_on_login_button()
        login.massage_eror_invalid_login()

        sleep(3)

    def test3_login_blank_username(self):
        self.driver.get("https://app.gozine2.ir/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        login.enter_password("0020421729")
        login.click_on_login_button()
        login.massage_eror_blank_usernamepassword()

        sleep(3)

    def test4_login_blank_password(self):
        self.driver.get("https://app.gozine2.ir/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        login.enter_username("7418700")
        login.click_on_login_button()
        login.massage_eror_blank_usernamepassword()

        sleep(3)

    def test5_login_blank_username_password(self):
        self.driver.get("https://app.gozine2.ir/Login?returnUrl=%2F")
        login = Login(driver=self.driver)
        login.click_on_login_button()
        login.massage_eror_blank_usernamepassword()

        sleep(3)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()
