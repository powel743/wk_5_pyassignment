#creating an empty list
my_list = []
print("initial list:", my_list)
#adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
#putting 15 on second place
my_list.insert(1, 15)
#adding othher elements at the end of the list
extended_elements = [50, 60, 70]
my_list.extend(extended_elements)
#removing the last element
my_list.pop()
#sorting list in ascending order
my_list.sort()
#finding and printing index of value 30 in my list
index_of_30 = my_list.index(30)
print("index of 30:", index_of_30)