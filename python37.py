#SINGLE INHERITANCE
class A:
    def __init__(self):
        print("hello world")
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B(A):
    def __init__(self):
        super().__init__()
        print("bye")
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")

a1=B()
