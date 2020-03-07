#!/usr/local/bin/python3.7

#class A(object):
class A():
    def whereiam(self):
        print("I am in A")

class B(A):
    def whoiam(self):
        print("I am B")

class C(A):
    def whereiam(self):
        print("I am in C")

class D(B, C):
    def whereiam(self):
        print("I am in D")

class E(B, C):
    def whoiam(self):
        print("I am E")

d = D()
d.whereiam()
e = E()
e.whereiam()
