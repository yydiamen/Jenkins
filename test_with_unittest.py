import unittest ,hamcrest
from Example import primitive_calc , person
class test_with_unittest(unittest.TestCase):
    def testMultiplyWithUnitTest(self):
        a = 5 
        b = 6 
        excepted = 30
        val = primitive_calc.multiply(a,b)
        self.assertEquals(excepted,val)
    def testWithPyHamcrest(self):
        a = 5
        expected  =  125
        val = primitive_calc.cube(a)
        hamcrest.assert_that(expected,hamcrest.equal_to(125))
    def testWithPerson(self):
        person_a = person("Dothan", 20,"Doti")
        person_b = person("David",20,"David")
        person_c = person("Dothan",20,"Mike")
        
        hamcrest.assert_that(person_a,hamcrest.equal_to(person_c))
        hamcrest.assert_that(person_a,hamcrest.is_not(person_b))
        hamcrest.assert_that(person_b,hamcrest.is_not(person_c))
if __name__ == '__main__':
    unittest.main()