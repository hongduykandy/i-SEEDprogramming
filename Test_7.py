#Problem 2
class Car:
    color = ""
    speed = 0

    def upSpeed(self, value): 
        self.speed +=value
        
        
#Problem 4
class Horse:
    speed = 0

    def upSpeed50(self):
        self.speed +=50

#Problem 6
class Car: 
    def method(self):
        print("Super Class")

class Sedan(Car):
    def method(self):
        print("Sub Class")

myCar = Car()
mySedan = Sedan()
myCar.method()
mySedan.method() 
 

#Problem 7
class Car:
    color = ""
    speed = 0

    def upSpeed(self, value):
        self.speed +=value

class RVCar(Car):
    seatNum = 0

    def getSeatNum(self):
        return self.seatNum      