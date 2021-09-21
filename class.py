# class Student(object):
#     def __init__(self, name, age, gender, level, grades=None):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.level = level
#         self.grades = grades or {}

#     def setGrade(self, course, grade):
#         self.grades[course] = grade

#     def getGrade(self, course):
#         return self.grades[course]

#     def getGPA(self):
#         return sum(self.grades.values())/len(self.grades)

# # Define some students
# john = Student("John", 12, "male", 6, {"math":93,"science":98})
# jane = Student("Jane", 12, "female", 6, {"math":3.5})

# # Now we can get to the grades easily
# print(john.getGPA())
# print(jane.getGPA())



class Car(object):
    def __init__(self,model,company,color,speed_limit):
        self.model = model,
        self.company = company,
        self.color = color,
        self.speed_limit = speed_limit
    def getDetails(self):
        print(self.company,self.model,self.color,"color",".Top speed is",self.speed_limit)
    def start(self):
        print("started")
    def stop(self):
        print("stoped")
    def accelerate(self):
        print("accelerating...")
        "accelerating functinality here"
    def change_gear(self,gear_type):
        print("gear changed")
        "gearing functinality here"


car1 = Car("bolero","mahindra","white","80mph")
car2 = Car("modelS","tesla","white","90mph")
car3 = Car("roadster","tesla","red","100mph")
car4 = Car("Q7","audi","grey","80mph")
car5 = Car("innova","toyota","black","80mph")
car6 = Car("harrier","tata","blue","80mph")
car7 = Car("civic","honda","red","80mph")
car8 = Car("S-class","benz","white","80mph")
print(car1.getDetails())        
print(car2.getDetails())        
print(car3.getDetails())        
print(car4.getDetails())        
print(car5.getDetails())        
print(car6.getDetails())        
print(car7.getDetails())        
print(car8.getDetails())        
print(car1.accelerate())        


