class students:
    university='sdmit'
    def __init__(self,m1,m2,m3):#constructor
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @classmethod#decorator
    def getschool(cls):
        return cls.university
    @staticmethod
    def info():
        print("welcome to sdmit")
    def avg(self):
        return(self.m1+self.m2+self.m3)/3
s1 = students(34,55,67)
s2 = students(34,88,90)


print(s2.avg())
print(s2.getschool())
students.info()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
