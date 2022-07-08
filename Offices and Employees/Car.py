class Car:
    
    def __init__(self, name, fuelRate, velocity):
        self.name = name
        self.fuelRate = fuelRate
        self.set_fuelRate(fuelRate)
        self.velocity = velocity
        self.set_velocity(velocity)
    
    def set_velocity(self, velocity):
        if self.velocity > 200:
            self.velocity = 200
            print("Maximum speed is 200 km/s")
        
        elif self.velocity < 0:
            self.velocity = 0
            
        else:
            self.velocity = self.velocity
    
    def __str__(self):
        return "he has a car model : {} , The amount of fuel: {} and with velocity: {}".format(self.name, self.fuelRate, self.velocity)
    
            
    def set_fuelRate(self, fuelRate):
        if self.fuelRate > 100:
            self.fuelRate = 100
            print("Maximum Amount of fuel Rate is 100. So fuelRate = {}".format(self.fuelRate))
        
        elif self.fuelRate < 0:
            self.fuelRate = 0
            
        else:
            self.fuelRate = self.fuelRate
     
   
    def run(self, distance):
        self.distance = distance
        self.fuelRate -= self.distance
        self.stop()
        
        
    def stop(self):
        if self.fuelRate < 0:
            print("You need to refuel \nThe remain distance to arrive is: {} Km".format(abs(self.fuelRate)))
              
        elif self.fuelRate == 0:
            print("You Arrived!! But you need to refuel")
            
        elif self.fuelRate > 0:
            print("You Arrived!!")
        
        self.velocity = 0
