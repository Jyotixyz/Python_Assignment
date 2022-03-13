Python 3.10.2 (v3.10.2:a58ebcc701, Jan 13 2022, 14:50:16) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#float ===> int bool str
a = 78.2
b = int(a)
print(a)
78.2
print(type(a))
<class 'float'>
print(b)
78
print(type(b))
<class 'int'>

#float to bool
a = 89.4
b = bool(a)
print(a)
89.4
print(type(a))
<class 'float'>
print(b)
True
print(type(b))
<class 'bool'>

#float to str
a = 67.3
b = str(a)
print(a)
67.3
print(type(a))
<class 'float'>
print(b)
67.3
print(typa(b))
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    print(typa(b))
NameError: name 'typa' is not defined. Did you mean: 'type'?
print(type(b))
<class 'str'>
