import unittest
from fall import basic,extend
class wcounttest(unittest.TestCase):
    def test_fbasic(self):
        testone=basic('c','2.txt')
        self.assertEqual(testone,203)
        testtwo=basic('w','2.txt')
        self.assertEqual(testtwo,38)
        testthree=basic('s','2.txt')
        self.assertEqual(testthree,4)
    def test_fexend(self):
        testfour=extend('k','3.txt')
        self.assertEqual(testfour,2)
        testfive=extend('z','3.txt')
        self.assertEqual(testfive,7)
        testsix=extend('d','3.txt')
        self.assertEqual(testsix,17)
unittest.main()
