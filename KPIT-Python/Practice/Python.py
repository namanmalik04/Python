print("Hello, World!")

print('Hello, World!')

name = "naman"
age  = 22

print("My name is " ,name , "My age is ", age)

#  age = input("Enter your age: ")

age = int(age) + 5
print("My name is " ,name , "My age is ", age)

print(True + True)
print(str(10) + "naman")

print (name.find('n'))

print (name.index('n'))

print (name.rfind('n'))

print (name.replace('a', 'o'))

print("na" in name)

print(5/2 , 5//2 , 5**2)

if age > 18:
    print("You can vote")
elif age < 18 and age > 12:
    print("You are a teenager")
else:
    print("You are a kid")

for i in range(5):
    print(i)

print()

for i in range(2, 10, 2):
    print(i)

s = "Hello World"

s.strip()

# a copy of s without leading or trailing whitespace

print(s.strip())

s.split('l')

print(s.split("l"))
 
s.splitlines()

# split ‘s’ into a list of strings, one per line

print(s.splitlines())

s.lower()

# a lowercased version of the string ‘s’

print(s.lower())

s.upper()

# an uppercased version of the string ‘s’

print(s.upper())

# text.join(s)
# combine the words of the text into a string using ‘s’ as the glue

print("*".join(s))

s.title()

# a title cased version of the string ‘s’

print(s.title())

# s.capitalize()

# converts first character of a ‘s’ to uppercase letter and lowercases all other characters

# print(s.capitalize())

# s.startswith()

# returns True if a string starts with the specified prefix(string). If not, it returns False

# print(s.startswith(“Welcome”))

# print(s.startswith(“come”,3,10))

# s.endswith()

# returns True if a string ends with the specified suffix. If not, it returns False

# print (s.endswith(“Session"))

# print (s.endswith("to",2,16))

# s.swapcase()

# s.isalnum()
# returns True if all characters in the string are alphanumeric (either alphabets or numbers). If not, it returns False
# print(s.isalnum())
# s1=“Python310”
# print(s1.isalnum())
# s.isalpha()
# returns True if all characters in the string are alphabets. If not, it returns False
# print(s.isalpha())
# s2="HelloPython"
# print (s2.isalpha())
# s.isdigit()
# returns True if all characters in a string are digits. If not, it returns False
# print (s.isdigit())
# s2="98564738"
# print (s2.isdigit())


# s.islower()
# returns True if all alphabets in a string are lowercase alphabets. If the string contains at least one uppercase alphabet, it returns False.
# print(s.islower())
# s1=“python”
# print(s1.islower())
# s.isupper()
# returns whether or not all characters in a string are uppercased or not
# print(s.alpha())
# s2="HelloPython"