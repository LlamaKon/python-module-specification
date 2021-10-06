# mymodule.py
"""
myvariable = 'This is global variable'

def myfunc():
	print('This is my function!')


def anotherfunc():
	print('This is another function!!')


if __name__ == '__main__':

	print('This is mymodule!!')
"""
# __main__

import mymodule

mymodule.myfunc()

# This is mymodule!!
# This is my function!

print(__name__)

# __main__