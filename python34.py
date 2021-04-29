class car:
    wheels=4#class variable
    def feature(self):
        self.model="BMW"#instance variable
        self.color="black"#instance variable
c1=car()
c2=car()
c1.feature()
c2.feature()
c1.model="A Star"
print(c1.model,c1.color,car.wheels)
print(c2.model,c2.color,car.wheels)
        
