Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(3==2+1)
True
>>> print(4<4)
False
>>> print(6>=6)
True
>>> print(-2<0)
True
>>> print(6>8 and 5>4)
False
>>> print(6>8 and 5>4 or 8<10)
True
>>> print((6>8 and (5>4 or 8<10)))
False
>>> x
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> x=4
>>> print(x==4)
True
>>> print(x=4)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(x=4)
TypeError: 'x' is an invalid keyword argument for print()
>>> a=100
>>> b="science"
>>> print(a>75 and b!="science")
False
