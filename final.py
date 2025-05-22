# --- Task1 ---
# name = input("Enter your name: ")
# print("Hello ",name)

# --- Task2 ---
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# sum = num1 + num2
# print("Sum is ",sum)

# --- Task3 ---
# temp_celsius = int(input("Enter temperature in celsius: "))
# temp_fahrenheit = temp_celsius * 9/5 + 32
# print("Temperature in fahrenheit is ",temp_fahrenheit)

# --- Task4 ---
# name = input("Enter your name : ")
# age = int(input("Enter your age : "))
# city = input("Enter name of your city: ")
# print(name,"is ",age,"years old and lives in ",city)

# --- Task5 ---
# num = int(input("Enter a number to print table: "))
# for i in range(1,11):
#     print(num," * ",i," = ",num*i)

# --- Task6 ---
# import pandas as pd 
# dict = {
#     'Name':['Zeeshan Nawaz','Nayab Gulshan','Ali'],
#     'Age': [20,20,21],
#     'City': ['Khushab','Khushab','Lahore']
# }
# dataframe = pd.DataFrame(dict)
# print(dataframe)

# --- Task 7 ---
# import pandas as pd
# dataFrame = pd.read_csv('students.csv')
# print(dataFrame.head())

# --- Task8 ---
# import pandas as pd
# dict = {
#     'Name':['Zeeshan Nawaz','Nayab Gulshan','Ali'],
#     'Age': [20,20,21],
#     'City': ['Khushab','Khushab','Lahore']
# }
# dataFrame = pd.DataFrame(dict)
# dataFrame.to_csv('output.csv')

# --- Task 9 ---
# list = [1,2,2,3,4,4,5]
# set = set(list)
# print(set)

# --- Task10 ---
# set1 = {1,2,3}
# set2 = {3,4,5}
# union = set1 | set2
# intersection = set1 & set2
# print("Union: ",union)
# print("Intersection: ",intersection)

# --- Task11 ---
# a = {1,2,3}
# b = {1,2,3,4,5}
# subset = a.issubset(b)
# print(subset)
# superset = b.issuperset(a)
# print(superset)

# --- Task12 ---
# import numpy as np
# array = np.array([10,20,30,40,50])
# print(array.shape)
# print(array.dtype)

# --- Task13 ---
# import numpy as np
# a = np.array([1,2,3])
# b = np.array([4,5,6])
# sum = np.add(a,b)
# multiply = np.multiply(a,b)
# print('Sum: ',sum)
# print('Multiply: ',multiply)

# --- Task14 ---
# class Person:
#     def __init__(self, name, age, salary):
#         self.name = name  
#         self._age = age  
#         self.__salary = salary  

#     def DisplayDetails(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self._age}")
#         print(f"Salary: {self.__salary}")

#     def _IncreaseAge(self):
#         self._age += 1

#     def __IncreaseSalary(self, amount):
#         self.__salary += amount

#     def PublicMethod(self, amount):
#       self.__IncreaseSalary(amount)
#       return self.__salary
    
# person1 = Person("Alice", 30, 50000)
# print("Public member name:", person1.name)
# print("Protected member age:", person1._age)
# person1.DisplayDetails()
# person1._IncreaseAge()
# print("Updated age:", person1._age)
# new_salary = person1.PublicMethod(5000)
# print("Updated salary:", new_salary)


    



