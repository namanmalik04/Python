d1=  {1:89 , 2:99 ,5:78 , 3:55 , 2:78,6:90,6:75,6:11,8:100,9:100}
print(d1)
print(d1.values())
print(set(d1.values()))
print(tuple(d1.values()))

d2={101:"Neha",201:"Varun",301:"Yash"}
d2[301]="Priya"  # if key already present it will overwrite value
d2[401]="Anil"   #if key not present, it will be added newly
print(d2)

d3={"Neha":101,"Varun":201, "Yash":301,"yash":601}
print(d3)
d4={101:"Rahul" , "Tina":"Reena", 102:34.55, 103:[55,66,77]}
print(d4["Tina"])  # access value using key with [] operator
print(d4[103])  
try:
    print(d4[400])#if key not present - gives keyError
except KeyError as k:
    print('Invalid key ',k)
print(d4.get(400,"not found"))
print(d4.get("Tina"))
print("d4.get(222)  ",d4.get(222)) #if not not present- no error - output is None
print(d4)
print(d4.items()) 
print(d4.keys())  # get all keys
print(d4.values()) #get all values
# key- 101 --> whether 101 key is present in given dict
if 101 in d4:
    print('key found')
else:
    print('key not found')

if d4.get(222) is  None:
    print('key not found')
else:
    print('key found')
try:
    if d4[101]:
        print('key found')
except :
    print('key not found')
try:
    if d4[999]:
        print('key found')
except:
    print('key not found')
# value="amit" --->whether "amit" value is present in given dict
print("value found -","Rahul" in d4.values())
d4={101:"Rahul" , "Tina":"Reena", 102:34.55, 103:[55,66,77]}
flag=False
for key in d4:
    #if d4[key]=="Rahul":
    if d4[key]==[55,66,77]:
        flag=True
        break
print('value found' if flag else 'value not found')
#---------------
if any([True for k,v in d4.items()  if v=="Rahul"] ):
    print('** value Found ')
else:
    print('** value Not Found ')

d5={1:[100,200] , (44,55,66):222}
print(d5)
# key can be either number/string/tuple
print('**********************')
d5={1:110,2:200,3:500,5:400,7:900,6:877}
del d5[2]  # gives an error if key not found otherwise deletes record with given key
print(d5)
print('popped value', d5.pop(1))# gives an error if key not found otherwise deletes record with given key
print(d5)
d5.popitem()# remove/pop last item from dictionary
#d5.pop(3)
print(d5)
d6={1:100,2:200,3:300,4:None}
print(len(d6))
print(len(d6.keys()))
print(len(d6.values()))
