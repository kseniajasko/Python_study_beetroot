# Create your own class, which can behave like a built-in function `open`.
# Also, you need to extend its functionality with counter and logging.
# Pay special attention to the implementation of `__exit__` method.
import logging

class File(object):

    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()

def write(text_1, file_1):
    with File(file_1, 'r+') as opened_file:
        opened_file.write(text_1)

write('Hola', 'demo.txt')
write('Hola1', 'demo.txt')


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

