import datetime
import json

class Office:
    
    num = 1
    
    def __init__(self,name, employees=[]):
        self.name = name
        self.employees = employees
        Office.num +=1
        self.JSON_write()
    
    
    def JSON_write(self):
        The_Office = {"Employees":self.employees}
        write_file = open("Offices.json", "w")
        data =json.dump(The_Office, write_file , default=lambda o: o.__dict__, indent=6 , sort_keys=True )
        write_file.close()
            
        
    def JSON_read(self):
        with open('Offices.json',) as read_file:
            json_object = json.load(read_file)
            print(json.dumps(json_object, default=lambda o: o.__dict__, indent=6 , sort_keys=True ))
    
    
    
    def get_all_employees(self):
        return self.employees
    
    
    def get_employee(self,empId):
        for self.employee in self.employees:
            if self.employee.Id == empId:
                return self.employee
    
    
    
    def hire(self, Employee):
        self.employees.append(Employee)
        with open('Offices.json',) as json_file:
            data = json.load(json_file)
            New_Employee = {"Employees":Employee}
            data.update(New_Employee)
            self.JSON_write()
        

    def fire(self , empId):
        self.employees.pop(empId)
        self.JSON_write()
        
    
    
    def deduct(self,empId,deduction):
        for self.employee in self.employees:
            if self.employee.Id == empId:
                self.employee.salary -= deduction
                
    
    
    def reward(self,empId,reward):
        for self.employee in self.employees:
            if self.employee.Id == empId:
                self.employee.salary += reward
      
    
                
    def check_lateness(self , empId, moveHour):
        for employee in self.employees:
            if employee.Id == empId:
                calc= Office.calculate_lateness(moveHour, employee.distanceToWork, employee.car.velocity)
    
                if calc == True:
                    employee.salary += 10
                    print("In the right time")
                else:
                    employee.salary -= 10
                    print("You are late!!!")
        
    @staticmethod
    def calculate_lateness(moveHour, distance, velocity):
        
        targetHour = datetime.datetime.strptime('09:00:00', '%H:%M:%S')
        Office.moveHour = moveHour
        moveHour = datetime.datetime.strptime(moveHour , '%H:%M:%S')
        time_to_arrive = ((distance) / (velocity))*1000
        time_to_arrive = datetime.datetime.fromtimestamp(time_to_arrive)
        time_zero = datetime.datetime.strptime('1970-1-1 02:00:00', '%Y-%m-%d %H:%M:%S')

        if ((time_to_arrive - time_zero)+moveHour) < targetHour:
            return True
        else:
            return False
        
        
        
    @classmethod
    def change_emps_num(cls):
        cls.num += 1
        print("We have {} Employees in the office".format(cls.num))
