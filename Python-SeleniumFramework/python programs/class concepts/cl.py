class MyClass:
    def __init__(self):
        print("inside constructor")

    def m1(self):
        print("another method")


class C2(MyClass):

    def __init__(self):
        MyClass.__init__(self)
    def m1(self):
	    print("inside second class")

obj1 = MyClass()
obj1.m1()
obj2 = C2()
obj2.m1()

