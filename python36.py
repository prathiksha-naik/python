class student:
    def __init__(self,name,usn):
        self.name=name
        self.usn=usn
        self.lap=self.innerclass()
    def show(self):
        print(self.name,self.usn)
        self.lap.show()
    class innerclass:
        def __init__(self):
            self.brand='hp'
            self.cpu='ryzen3'
            self.ram=8
        def show(self):
            print(self.brand,self.cpu,self.ram)

s1=student('prathi',3)
s2=student('prarthu',5)
s1.show()
