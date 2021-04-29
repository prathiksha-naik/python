class computer:
    def __init__(self):
        self.name="prathiksha"
        self.age=28
    def compare(self,comp2):
        if self.age==comp2.age:
            print("true")
        else:
            print("false")
comp1=computer()
comp2=computer()
comp2.age=33
comp2.compare(comp1)
