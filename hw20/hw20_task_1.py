# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of `__exit__` method.
import logging
from os import path

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

class File(object):
    counter = 0

    @classmethod
    def get_counter(cls):
        return cls.counter

    def __init__(self, file_name, method):
        File.counter += 1
        self.file_obj = open(file_name, method)
        logging.warning(f'Getting the parametres: {File.counter}')

    def __enter__(self):
        logging.warning(f'Opens the file and returns it: {File.counter}')
        return self.file_obj

    def __exit__(self, type, value, traceback):
        logging.warning(f'Closes the file: {File.counter}')
        self.file_obj.close()

def write(text_1: str, file_1: str):
    with File(file_1, 'a') as f_1:
        f_1.write(f'{text_1}\n')

def reads(file_2: str):
    if not path.isfile(file_2):
        raise FileNotFoundError(f'The file "{file_2}" does not exist')

    with File(file_2, 'r+') as f_2:
        a = f_2.read()
        return a

if __name__ == '__main__':
    write('One', 'demo.txt')
    #write('Two', 'demo.txt')
    reads('demo.txt')
    reads('demo1.txt')

    print(File.get_counter())


# 1) The with statement stores the __exit__ method of the File class.
# 2) It calls the __enter__ method of the File class.
# 3) The __enter__ method opens the file and returns it.
# 4) The opened file handle is passed to opened_file.
# 5) We write to the file using .write().
# 6) The with statement calls the stored __exit__ method.
# 7) The __exit__ method closes the file.

# Our __exit__ method accepts three arguments. They are required by every __exit__ method
# which is a part of a Context Manager class.
# Between the 4th and 6th step, if an exception occurs,
# Python passes the type, value and traceback of the exception to the __exit__ method.
# It allows the __exit__ method to decide how to close the file and if any further steps are required.
# In our case we are not paying any attention to them.

