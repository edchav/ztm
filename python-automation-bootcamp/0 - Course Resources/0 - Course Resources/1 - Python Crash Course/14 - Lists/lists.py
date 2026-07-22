#create a list
my_list = [1,2,3,4,5]

#access the first list item
my_list[0]

#create a list with mixed data types
mixed_list = [1,"two",3.0,["four",5]]

#access the fourth item from mixed list
mixed_list[3]

#access the first item in the list nested inside mixed_list
mixed_list[3][0]

#append a new item (also a list) to mixed_list
mixed_list.append([6.0,'seven'])

#get the length of a list
len(mixed_list)
