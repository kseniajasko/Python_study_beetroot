import unittest
import hw20_task_1

class TestTaskOne(unittest.TestCase):

    def test_add(self):
        file_test = 'demo.txt'
        test_text = 'Hola'
        hw20_task_1.write(test_text, file_test)
        f_1 = open(file_test, 'r+')
        a_1 = f_1.readline()
        print(a_1)
        self.assertEqual(test_text, a_1)

unittest.main()