import unittest
import os
from time import sleep
import EstimateRank.Tests.CalculateTest
import EmailReport.Email
from TestRunner import HTMLTestRunner
import Login.Tests.LoginTest

current_directory = os.getcwd()


class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_All(self):
        # Create a TestSuite comprising the two test cases
        suit = unittest.TestSuite()

        # Add the test cases to the Test Suite
        suit.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login.Tests.LoginTest.LoginTests),
            unittest.defaultTestLoader.loadTestsFromTestCase(EstimateRank.Tests.CalculateTest.CalculateTest)

        ])

        report = current_directory + "\HTML_Test_Runner_ReportTest.html"
        with(open(report, 'wb')) as fp:
            runner = HTMLTestRunner(
                stream=fp,
                title='Unit Test report',
                description='unit test'
            )
            runner.run(suit)

            sleep(50)

    email = EmailReport.Email.Email()
    print(email.send_email())


if __name__ == '__main__':
    unittest.main()
