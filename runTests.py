import argparse
import os
import unittest
import HTMLTestRunner
from Tests.TestClass import TestClass


def runTests():
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)


def runTests_with_report():
    dir = os.getcwd()
    reportFile = open(dir + "\Test_Report.html", "w")
    runner = HTMLTestRunner.HTMLTestRunner(stream=reportFile, title='Test Report',
                                           description='Report from executed UI Tests')
    runner.run(test_suite)


testCases_group1 = unittest.TestLoader().loadTestsFromTestCase(TestClass)
test_suite = unittest.TestSuite()
test_suite.addTest(testCases_group1)

parser = argparse.ArgumentParser(description='Selenium tests')
parser.add_argument('--report', '-r', help='Generate output html report', action="store_true")
args = vars(parser.parse_args())

if args['report']:
    runTests_with_report()
else:
    runTests()
