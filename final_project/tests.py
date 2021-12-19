import unittest
from ticky_check import *

class Ticky(unittest.TestCase):

    def test_info_dict(self):
        info_sample = {
            'User': 'ac', 'INFO': 2, 'ERROR': 2,
            'User': 'ahmed.miller', 'INFO': 2, 'ERROR': 4,
            'User': 'blossom', 'INFO': 2, 'ERROR': 6,
            'User': 'bpacheco', 'INFO': 0, 'ERROR': 2,
            'User': 'breee', 'INFO': 1, 'ERROR': 5,
            'User': 'britanni', 'INFO': 1, 'ERROR': 1,
            'User': 'enim.non', 'INFO': 2, 'ERROR': 3,
            'User': 'flavia', 'INFO': 0, 'ERROR': 5,
            'User': 'ac', 'INFO': 2, 'ERROR': 2,
        }
        info = info_processing(file_contents)
        self.assertEqual(info, info_sample)

    def test_error_dict(self):
        error_sample = {
            'Error': 'Timeout while retrieving information', 'Count': 15,
            'Error': 'Connection to DB failed', 'Count': 13,
            'Error': 'Tried to add information to closed ticket', 'Count': 12,
            'Error': 'Permission denied while closing ticket', 'Count': 10,
            'Error': 'The ticket was modified while updating', 'Count': 9,
            'Error': 'Ticket doesn\'t exist', 'Count': 7
        }
        errors = error_processing(file_contents)
        self.assertEqual(errors, error_sample)

if __name__ == '__main__':
    unittest.main()
