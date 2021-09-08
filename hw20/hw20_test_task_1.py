import unittest
import hw20_task_1
import logging

class TestTaskOne(unittest.TestCase):

    def test_add(self):
        file_test = 'demo.txt'
        test_text = f'Two\n'
        hw20_task_1.write(test_text, file_test)
        with open(file_test, 'r+') as f_1:
            a_1 = f_1.readline()
        #a_1 = hw20_task_1.reads(file_test)
        self.assertEqual(test_text, a_1)

unittest.main()