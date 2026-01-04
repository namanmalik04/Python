def calength(n1 : str)->int :
    if isinstance(n1,str):
        return len(n1)
    
print(calength("KPIT"))


def getvalue(n):
    if n<100:
        return n

value = getvalue(200)
print(value)


def display(age,city,personname):
    print(age,city,personname)

display(personname="John",city="Pune",age=25)