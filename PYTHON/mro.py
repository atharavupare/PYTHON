#!/usr/local/bin/python3.7

#class A(object):
class A():
    def whereiam(self):
        print("I am in A")

class B(A): #Class B inheriting from A
    def whoiam(self):
        print("I am B")

class C(A): #Class C inheriting from A
    def whereiam(self):
        print("I am in C")

class D(B, C): #Class D inheriting from B and C
    def whereiam(self):
        print("I am in D")

class E(B, C): #Class E inheriting from B and C
    def whoiam(self):
        print("I am E")

d = D()
d.whereiam()
e = E()
e.whereiam()

# OUTPUT:
# sbshark@pop-os:~/github/PYTHON$ python3 mro.py #initialy
# I am in D
# I am in C
# sbshark@pop-os:~/github/PYTHON$ python3 mro.py #after commenting D class
# I am in C
# I am in C
# sbshark@pop-os:~/github/PYTHON$ python3 mro.py #after commenting C class
# I am in A
# I am in A
