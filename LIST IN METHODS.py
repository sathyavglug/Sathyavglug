# Simple list creation 

list_1=[24,5,9,32,3,2,7,6,3,35]
print("list 1 : ",list_1)

#list to find index and also list  accept multiple datatypes

list_of_data=[7,"java",(22,3,43,5),{"name":"sathya",'age':"18"},18.5,True,{"sathya","murthy","eighteen"}]
print("list of data : ",list_of_data)
print("0st index : ",list_of_data[0])
print("1nd index : ",list_of_data[1])
print("2rd index : ",list_of_data[2])
print("3th index : ",list_of_data[3])
print("4th index : ",list_of_data[4])
print("5th index : ",list_of_data[5])
print("6th index : ",list_of_data[6])


#To find the length of the list

length_of_the_list=len(list_of_data)
print("length of the list : ",length_of_the_list)

#to find maximum and minimum methods in lists

str_list=["sathya","sam","smith","vimal","apple","zebra"]
number_list=[34,6,34.6,3,64,245,6432.3,57,86,33]

min_str_list=min(str_list)
print(f"minimum in string list : {min_str_list}")
max_str_list=max(str_list)
print(f"maximum in string list : {max_str_list}")
min_num_list=min(number_list)
print(f"minimum in number list : {min_num_list}")
max_num_list=max(number_list)
print(f"maximum in number list : {max_num_list}")

#insertion method in list

list_for_insertion=["sathya","murthy","eighteen","tamilnadu","india"]
print("befoore insertion :" ,list_for_insertion)
list_for_insertion.insert(2,"jeeva")
print("after insertion :",list_for_insertion)

#poping in lists

list_for_pop=["ipl","dhoni","seven","tamilnadu","india"]
print("before pop: ",list_for_pop)
list_for_pop.pop()
print("after pop: ",list_for_pop)

#remove() in list

list_for_remove=["chennai","mumbai","dubai","dehli","goa"]
print("before removing :",list_for_remove)
list_for_remove.remove("dubai")
print("after removing :",list_for_remove)

#appending on list

list_for_append=["peter","john",827.76,"lawrence","mubarak",52]
print("before appending :",list_for_append)
list_for_append.append("jenifer")
print("after appending :",list_for_append)

#sorting in list
# 1. string list sortig

sorting_list=["pen","paper","notebook","xerox","apple"]
print("before sorting :",sorting_list)
sorting_list.sort()
print("after sorting:",sorting_list)

# counting in list
count_list=[8,5,3,2,6,1,4,21,2,34,5,2] 
print("before counting :",count_list)
a=count_list.count(2)
print("after counting 2 in list :",a)

#2.number list sorting

sorting_list=[36,64,3,42.23,521.3,1000,23,53.5,26]
print("before sorting :",sorting_list)
sorting_list.sort()
print("after sorting:",sorting_list)

#extend method in list

sample_list_1=["ant","scoropin","snake","crab","spider"]
sample_list_2=[56,35,47,73,46,38]
print(f"before extending : \n{sample_list_1}\n{sample_list_2}")
sample_list_1.extend(sample_list_2)
print("after extending  :",sample_list_1)

#list constructor()

# 1. str to list convertion

sample='foundation'
convert=list(sample)
print("string to list convert :",convert)

# 2. tuple to list convertion

sample_2=(2,4,5,6,3)
convert=list(sample_2)
print("tuple to list convertion: ",convert) 

# 3.dictionary to list convvertion

sample_3={"name":"sathya","age":18}
convert=list(sample_3) 
print("dict to list convertion : ",convert)

# sets to list convertion

sample_4={"sathya","raja",25,89,"ganesh"}
convert=list(sample_4)
print("sets to list convertion :",convert)

#int to list convertion

sample_5=3,2,4,54,2
convert=list(sample_5) 
print("int to list convertion : ",convert)

# list comprehension - to create  another new list from list

list_1=[8,5,3,2,6,1,4,21] # the list
print("previous first list :",list_1)
list_2=[s**2 for s in list_1] # newly created from previous list
print("newly created list : ",list_2)

list_3=["even" if x%2==0 else "odd" for  x in list_2]
print("list_2 is (odd /even): ",list_3)


