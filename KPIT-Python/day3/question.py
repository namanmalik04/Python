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