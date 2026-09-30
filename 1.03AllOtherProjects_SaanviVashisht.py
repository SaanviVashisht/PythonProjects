Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("1")
1
print(1)
1
print(1+2)
3
print(5+9)
14
print("1"+"2")
12
print("ha"*3+"!")
hahaha!
print("this"+" "+"is"+" "+"a"+"sentence"+".")
this is asentence.
print("this"+" "+"is"+" "+"a"+" "+"sentence"+".")
this is a sentence.
type(print(1))
1
<class 'NoneType'>
type(print("1"))
1
<class 'NoneType'>
type(1)
<class 'int'>
>>> type("1")
<class 'str'>
>>> print("6"+2)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print("6"+2)
TypeError: can only concatenate str (not "int") to str
>>> print("6"*2)
66
>>> print("6"+" "+"2")
6 2
>>> print(6+2)
8
>>> print("6"+"2")
62
>>> print(12)
12
>>> 
>>> animal = "dogs"
>>> print(animal+ " are really cool.")
dogs are really cool.
>>> print(dogs+"are cool.")
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(dogs+"are cool.")
NameError: name 'dogs' is not defined
>>> age=5
>>> print("Onyx is "+age)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print("Onyx is "+age)
TypeError: can only concatenate str (not "int") to str
>>> age=5
>>> print("Onyx is"+str(age))
Onyx is5
>>> type(age)
<class 'int'>
>>> type(str(age))
<class 'str'>


