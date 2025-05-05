num_list = [1,2,3,4,5,6,7,8,9,10] #initialize a list of numbers from 1 to 10
print(f"Original list: {num_list}")
list_1 = num_list[:5] # slicing upto position 5 but not including
print(f"Extracted first 5 elements: {list_1}")
list_1.reverse() #reverses the list but not returns anything
print(f"Reversed extracted elements: {list_1}")
