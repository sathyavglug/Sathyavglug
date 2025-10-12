my_dict={"name":"sathya",
         "age":10,
         "city":"chennai",
         "planet":"earth"}
print(my_dict)

# deletion 
del my_dict["planet"]
print(my_dict)
del my_dict["age"]
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
# addition
my_dict["state"]="tamilnadu"
print(my_dict)
#replace
my_dict["earth"]="mars"
print(my_dict)

#use for loop to iterate the elments
print()
for i in my_dict:
    print(i)
print()
for i in my_dict.values():print(i)
print()
#while loops
my_dict={"name":"sathya",
         "age":10,
         "city":"chennai",
         "planet":"earth"}
data=list(my_dict.values())
data2=list(my_dict.keys())  
i=0
while i < len(data):
    key=data[i]
    key2=data2[i]
    print(key)
    i+=1









5
