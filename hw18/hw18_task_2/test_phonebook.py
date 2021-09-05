import json
import unittest
import phonebook_methods

class TestPhonebookMethods(unittest.TestCase):
    def setUp(self):
        with open('data_phonebook.json', 'r') as f:
            self.data = json.load(f)

    def tearDown(self):
        with open('data_phonebook.json', 'w') as f:
            json.dump([], f, indent=4)

    def test_add(self):
        test_add_data = phonebook_methods.add('0956380996', 'Ok', 'Sat', 'Kyiv')
        self.setUp()
        self.assertEqual(test_add_data, self.data)

unittest.main()