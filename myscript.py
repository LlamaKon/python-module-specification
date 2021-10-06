# 標準ライブラリ
# サードパーティライブラリ
# 自作ライブラリ
# ローカルライブラリ


# mymodule.py
"""
myvariable = 'This is global variable'

def myfunc():
	print('This is my function!')


def anotherfunc():
	print('This is another function!!')

"""

import sys
sys.path.append("/Users/hibikikondo/Documents/001_program/000_specification/specification/python-function-specification")

import docstring

	# multiply num1 with num2 and return the result
	# :param num1: first number that you want to multiply
	# :param num2: first number that you want to multiply
	# :return: num1 * num2




	# num1 is devided by num2 and return the result
	# Args:
	# 	num1: first number that you want to multiply
	# 	num2: seconde number that you want to multiply

	# Returns:
	# 	num1 / num2


from mymodule import myfunc, myvariable, anotherfunc
# from mymodule import *
# import mymodule as m



myfunc()
anotherfunc()
print(myvariable)

# This is my function!
# This is another function!!
# This is global variable


"""
import mymodule

mymodule.myfunc()
mymodule.anotherfunc()
print(mymodule.myvariable)

# This is my function!
# This is another function!!
# This is global variable
"""

print(docstring.multiply(3, 4))

# 12
