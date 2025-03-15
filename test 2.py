Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> m='math kangaroo'
>>> print (f" {m} is fun.")
 math kangaroo is fun.
>>> p='python'
>>> w='Woohoo!'
>>> print (f" {w} I just learned {p}")
 Woohoo! I just learned python
>>> type -1
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    type -1
TypeError: unsupported operand type(s) for -: 'type' and 'int'
>>> type '-1'
SyntaxError: invalid syntax
>>> type 1
SyntaxError: invalid syntax
>>> type "1"
SyntaxError: invalid syntax
>>> type 1
SyntaxError: invalid syntax
>>> type
<class 'type'>
>>> '1'
'1'
>>> class '1'
SyntaxError: invalid syntax
>>> class supercalifragilisticexpialidoucious
SyntaxError: invalid syntax
>>> s='supercalifragilisticexpialidoucious'
>>> w='wonderful'
>>> print (f" {s}={w}. ")
 supercalifragilisticexpialidoucious=wonderful. 
>>> print (f" {w}")
 wonderful
>>> 