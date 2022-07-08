from Employee import Employee
from Car import Car
from Office import Office



# This is Some examples on Employees if you want to try the code
Samy= Employee('Samy' , 2150 , 'Lazy' , 25 , 1 , Car('fiat128' , 100 , 5), 'a@a.com' , 1000 , 20)
Adnan = Employee('Adnan' , 8000 , 'happy' , 50 , 2 , Car('BMW' , 100 , 20), 'a@a.com' , 2500 , 200)
Mahmoud = Employee('Mahmoud' , 5000 , 'tired' , 25 , 3 , Car('TOYOTA' , 100 , 10), 'a@a.com' , 2000 , 50)
emp_abudy= Employee('Abudy' , 210 , 'Lazy' , 33 , 4 , Car('fiat128' , 150 , 10), 'a@a.com' , 900 , 10)
emp_Yusri =Employee('Yusri' , 2210 , 'Lazy' , 58 , 5 , Car('fiat12' , 50 , 5), 'a@a.com' , 9500 , 35)

#This is all methods on ((  Person  )) class running on Samy  
Samy.sleep(7)
Samy.eat(3)
Samy.buy(2)

#Watch the difference on Samy before and now
print(Samy)

#This is some methods on ((  Employee  )) class running on Samy
#the distance = 20
Samy.drive(20)

#Now the fuelRate now is decreased by 20%
print(Samy.car.fuelRate)

#If you want to refuel 
Samy.refuel()
print(Samy.car.fuelRate)




#This is ((  Office )) within employees work in it
ITI = Office('ITI' ,[Samy , Adnan , Mahmoud])

# #To read a created JSON file 
ITI.JSON_read()

# #To hiring a new employee and adding to JSON file
ITI.hire(emp_abudy)

# #To check new employee is added or not 
ITI.JSON_read()

#To get specific employee on this office
print(ITI.get_employee(1))

#To fire some employee
ITI.fire(1)

#Finally if you want to check lateness on specific employee
ITI.check_lateness(1 , '7:50:00')

#To check number of employess on this office 
ITI.change_emps_num()