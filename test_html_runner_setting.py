import unittest
import os

# Import the HTMLTestRunner Module
import EstimateRank.Tests.CalculateTest
import Login.Tests.LoginTest


# Get the Present Working Directory since that is the place where the report
# would be stored
import HtmlTestRunner

current_directory = os.getcwd()


class HTML_TestRunner_TestSuite(unittest.TestCase):
    def test_All(self):
        # Create a TestSuite comprising the two test cases
        consolidated_test = unittest.TestSuite()

        # Add the test cases to the Test Suite
        consolidated_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login.Tests.LoginTest.LoginTests),
            unittest.defaultTestLoader.loadTestsFromTestCase(EstimateRank.Tests.CalculateTest.CalculateTest)
        ])

        output_file = open(current_directory + "\HTML_Test_Runner_ReportTest.html", "w")

        html_runner = HtmlTestRunner.HtmlTestRunner(
            stream=output_file,

        )

        html_runner.run(consolidated_test)


if __name__ == '__main__':
    unittest.main()
