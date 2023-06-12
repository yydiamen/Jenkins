from hamcrest import *
import unittest
def build(string1, string2):
    return string1 + " " + string2
class TestStringBuilder(unittest.TestCase):
    def testString(self):
        string = build("Hello", "World")
        expected = "Hello World"
        assert_that(string, equal_to(expected))
        print(string)
    def testBuilder(self):
        string = build("", "")
        expected = " "
        assert_that(string, equal_to(expected))
        print(string)
if __name__ == '__main__':
    unittest.main()