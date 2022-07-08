from Person import Person
class Employee(Person):
    
    def __init__(self, name, money, mood, healthRate, Id, car, email, salary, distanceToWork):
        Person.__init__(self, name, money, mood, healthRate)
        self.Id = Id
        self.car = car
        self.email = email
        self.salary = salary
        self.set_salary(salary)
        self.distanceToWork = distanceToWork
        
    
    
    def set_salary(self, salary):
        if self.salary < 1000:
            print("Should minimum salary is 1000")
            self.salary = 1000
        else:
            self.salary = self.salary
    
    
    def __str__(self):
        return "The name of Employee is: {} Id number is: {},he carrying with him {}, mood: {}, rate of health: {}, have a car model: {}, email: {}, salary: {}, the distance to work {} km/s".format(self.name , self.Id , self.money , self.mood , self.healthRate, self.car, self.email, self.salary, self.distanceToWork)

    def __len__(self):
        return self.Id
            
    def work(self,work_hours):
        self.work_hours = work_hours
        if work_hours == 7:
            self.mood = "happy"
        elif work_hours < 7:
            self.mood = "tired"
        elif work_hours > 7:
            self.mood = "Lazy"
            
           
    def drive(self, distance):
        self.distance = distance
        self.car.run(distance)
                
    
    def refuel(self,gasAmount = 100):
        self.car.fuelRate = gasAmount
    
