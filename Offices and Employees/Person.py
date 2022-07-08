class Person:
    
    
    #Instructor method
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate =healthRate
        self.set_healthRate(healthRate)

        
    #To set the health rate between 0 - 100 
    def set_healthRate(self, healthRate):
        if self.healthRate > 100:
            self.healthRate = 100
            print("Should Health Rate between 0 - 100")
            
        elif self.healthRate < 0:
            self.healthRate = 0
            print("Should Health Rate between 0 - 100")
            
        else:
            self.healthRate = self.healthRate    
        
        
    def __str__(self):
        return "The name of person is: {} and he carrying with him {}, mood: {}, and rate of health: {}".format(self.name, self.money, self.mood, self.healthRate)
    
        
        
    def sleep(self,sleep_hours):
        self.sleep_hours = sleep_hours
        if sleep_hours == 7:
            self.mood = "happy"
        elif sleep_hours < 7:
            self.mood = "tired"
        elif sleep_hours > 7:
            self.mood = "Lazy"
          
        
    def eat(self, meals_number):
        self.meals_number = meals_number
        if meals_number == 3:
            self.healthRate = 100
        elif meals_number == 2:
            self.healthRate = 75
        elif meals_number == 1:
            self.healthRate = 50
        else:
            self.healthRate = 0
            print("Your Health in Danger")
         
        
    def buy(self , item):
        self.item = item
        self.money -= (self.item *10)
        return self.money
    