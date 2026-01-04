a=10
print(type(a))

print(10+20)

print("Manish"+"Manish")

print(10.5+20.5)

print()

True+True

print(10+"Radha")

TypeError : for +: ' int ' and str

print(10+True)

print(10.5+False)

print(10+10.5)
 
print(

int ( OutPut 123

print(

int ( OutPut 1

print(

int ( OutPut 0

print(float(False))

OutPut 0.0

print(

str ( OutPut False

a

, b = 10, 20

print(

str ( str ( OutPut 1020

print(

int (" OutPut 10

print(float("10"))

OutPut 10.0

print(

int ("10.6")) ValueError : invalid literal for int ()

with base 10: '10.6’
 
s.find(t)

index of first instance of string ‘t’ inside ‘s’ (-1 if not found)

print(s.find(“l”))

s.rfind(t)

index of last instance of string ‘t’ inside ‘s’ (-1 if not found)

print(s.rfind(“l”))

s.index(t)

like s.find(t) except it raises ValueError if not found

print(s.index(“o”))

s.rindex(t)

like s.rfind(t) except it raises ValueError if not found

print(s.rindex(“o”))

s.strip()

a copy of s without leading or trailing whitespace

print(s.strip())

s.split(t)

split ‘s’ into a list wherever a ‘t’ is found (whitespace by default)

print(s.split(“l”))
 
s.splitlines()

split ‘s’ into a list of strings, one per line

print(s.splitlines())

s.lower()

a lowercased version of the string ‘s’

print(s.lower())

s.upper()

an uppercased version of the string ‘s’

print(s.upper())

text.join(s)

combine the words of the text into a string using ‘s’ as the glue

print(“*”.join(s))

s.title()

a title cased version of the string ‘s’

print(s.title())

s.replace(t, u)

replace instances of ‘t’ with ‘u’ inside s

print(s.replace(“Python”, “Java”))
 
s.capitalize()

converts first character of a ‘s’ to uppercase letter and lowercases all other characters

print(s.capitalize())

s.startswith()

returns True if a string starts with the specified prefix(string). If not, it returns False

print(s.startswith(“Welcome”))

print(s.startswith(“come”,3,10))

s.endswith()

returns True if a string ends with the specified suffix. If not, it returns False

print (s.endswith(“Session"))

print (s.endswith("to",2,16))

s.swapcase()

converts all uppercase characters to lowercase and all lowercase characters to uppercase characters

print(s. swapcase() )


s.isalnum()
returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False
print(s.isalnum())
s1=“Python310”
print(s1.isalnum())
s.isalpha()
returns True if all characters in the string are alphabets. If not, it returns False
print(s.isalpha())
s2="HelloPython"
print (s2.isalpha())
s.isdigit()
returns True if all characters in a string are digits. If not, it returns False
print (s.isdigit())
s2="98564738"
print (s2.isdigit())


s.islower()
returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
print(s.islower())
s1=“python”
print(s1.islower())
s.isupper()
returns whether or not all characters in a string are uppercased or not
print(s.alpha())
s2="HelloPython"
print (s2.isalpha())
s.isspace()
returns True if there are only whitespace characters in the string. If not, it return False.
print (s.isspace())
s2=“ "
print (s2.isspace())


# check number is palindrome or not
# fibonacii series
# check prime    
#sum of first 5 odd numbers [1,3,5,7,9]=25
#sum of first 5 even numbers 2+4+6+8+10
# print first 10 prime numbers-- 2,3,5,7,11,13,17,19,23,29

# sum of digits of a number
 
# reverse the number
 
# calculate frequency of each digit in the number

''' 
 Reverse the order of elements in a list without using the reverse() method or slicing [::-1].
Example: [1, 2, 3] -> [3, 2, 1]
 
Check if a specific element exists in a list.
 
Remove duplicate elements from a list, maintaining the original order of the remaining elements.
 
Concatenate two lists into a single list. Do not use the + operator.
 
Create a new list that contains each element of an existing list repeated a certain number of times.
 
Given two lists, find the elements that are present in both.
 
Use list comprehension to create a new list containing only the even numbers from a given list.
 
Use list comprehension to create a new list containing the squares of only the odd numbers from a given list.
 
Given a list of lists, flatten it into a single list.
Example: [[1, 2], [3, 4], [5]] -> [1, 2, 3, 4, 5]
 
Rotate a list to the right by n positions.
Example: [1, 2, 3, 4, 5], n = 2 -> [4, 5, 1, 2, 3]
 
Given a list of integers, group consecutive numbers into sublists.
Example: [1, 2, 3, 5, 6, 7, 8, 9] -> [[1, 2, 3], [5, 6, 7, 8, 9]]

Merge two sorted lists into a single sorted list without using the built-in sort() method.
