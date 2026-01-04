'''
Lambdas in Python are small, anonymous functions that can be defined inline within a larger expression. 
They are a shorthand way to create small functions without having to declare a full-fledged function with a name.

Syntax
lambda arguments: expression

Lambdas are often used in situations where a small, one-time-use function is needed, such as:

As an argument to a higher-order function (a function that takes another function as an argument)
As a return value from a function
As a way to create a small, inline function without cluttering up the code with a separate named function
Some common use cases for lambdas include:

Sorting lists of objects based on a specific attribute
Filtering lists of objects based on a specific condition
Mapping a function over a list of objects
'''

numbers = [14, 21, 35, 40, 50, 66]
# Define a lambda function that checks if a number is odd
is_odd = lambda x: x % 2 != 0
# Use the lambda function as an argument to the filter() function
odd_numbers = list(   filter(is_odd, numbers) )
print(odd_numbers)  # prints [1, 3, 5]

# We can also define the lambda function directly as an argument to the filter() function, like this:
numbers = [1, 2, 3, 4, 5, 6]
# Use a lambda function as an argument to the filter() function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # prints [1, 3, 5]

#Example:As an argument to a higher-order function
objects = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_objects = sorted(objects, key=lambda x: x['age'])
print(sorted_objects)  # prints [{'name': 'Bob', 'age': 20}, {'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]


#objects = [{'name': 'John', 'age': 25,'exp':40}, {'name': 'Jane', 'age': 30,'exp':2}, 
#{'name': 'Bob', 'age': 20,'exp':30}]



a=[1,2,3,5]
r= list(  map(lambda x:x**2,a)  )
print(r)


from functools import reduce
sumnumbers = lambda x, y: x + y
#print(sumnumbers(3, 4))
l1=[1,2,3,4,5,22,10,20,11]
#resultlist=reduce(sumnumbers,l1)
resultlist=reduce(lambda x,y:x+y , l1)
print("Sum of list elements =",resultlist)
#print('sum of numbers in list =',sum(l1))


v = lambda x, y: x - y
l1=[20,1,3,2]
result = reduce(v,l1)
print("result = ",result)


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))#make square of each element
print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter odd elements
print(even_numbers)

#Convert each string to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))#convert to upper case
print(uppercase_fruits)

# # Calculate the area of each rectangle
rectangles = [(2, 3), (4, 5), (6, 7)]
areas = list(map(lambda x: x[0] * x[1], rectangles)) 
print(areas) 

# from functools import reduce
numbers = [7, 2, 6, 1, 4]
product = reduce(lambda x, y: x * y, numbers) #multiply elements 
print(product)


fruits = ['apple', 'banana', 'cherry', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))#get elements which starts with a
print(a_fruits)

people = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
twenty_five_year_olds = list(filter(lambda x: x['age'] == 25, people))
print('twenty_five_year_olds', twenty_five_year_olds)


students = [
    {'name': 'John', 'age': 20},
    {'name': 'Ajay', 'age': 22},
    {'name': 'Bob', 'age': 19},
    {'name': 'Anay', 'age': 31},
    {'name': 'John', 'age': 25}
]
students.sort(key=lambda x: x['age'])
print(students)

# fruits = {'apple': 5, 'banana': 10, 'cherry': 15}
# double_fruits = {k: lambda x: x*2 for k, x in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': <function <lambda> at 0x7f937f16c1f0>, 'banana': <function <lambda> at 0x7f937f16c280>, 'cherry': <function <lambda> at 0x7f937f16c310>}
# double_fruits = {k: v*2 for k, v in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': 10, 'banana': 20, 'cherry': 30}

from functools import reduce

# Sample dataset
vehicles = [
    {"id": 1, "fuel_efficiency": 25, "engine_power": 220, "transmission": "automatic"},
    {"id": 2, "fuel_efficiency": 30, "engine_power": 180, "transmission": "manual"},
    {"id": 3, "fuel_efficiency": 20, "engine_power": 250, "transmission": "automatic"},
    {"id": 4, "fuel_efficiency": 35, "engine_power": 200, "transmission": "manual"},
    {"id": 5, "fuel_efficiency": 28, "engine_power": 230, "transmission": "automatic"},
]

#Calculate the average fuel efficiency with automatic transmission:
automatic_vehicles = [x for x in vehicles if x["transmission"] == "automatic"]
print(automatic_vehicles)

fuel_efficiencies = [x["fuel_efficiency"] for x in automatic_vehicles]
print('eff',fuel_efficiencies)
total=0
for i in fuel_efficiencies:
       total+=i 
average_fuel_efficiency = total/len(fuel_efficiencies)
print("Average fuel efficiency of automatic vehicles:", average_fuel_efficiency)




#Remove vehicles with engine power less than 200 horsepower
filtered_vehicles = list(filter(lambda x: x["engine_power"] >= 200, vehicles))
print("Vehicles with engine power >= 200 horsepower:")
for vehicle in filtered_vehicles:
    print(vehicle)

#Map the transmission type to a numerical value (0 for automatic, 1 for manual)
transmission_map = {"automatic": 0, "manual": 1}
mapped_vehicles = list(map(lambda x: {**x, "transmission_code": transmission_map[x["transmission"]]}, vehicles))
print("Vehicles with transmission code:")
for vehicle in mapped_vehicles:
    print(vehicle)

# Reduce the dataset to only include vehicles with the highest fuel efficiency
max_fuel_efficiency = reduce(lambda x, y: x if x["fuel_efficiency"] > y["fuel_efficiency"] else y, vehicles)
print("Vehicle with the highest fuel efficiency:")
print(max_fuel_efficiency)


 




 