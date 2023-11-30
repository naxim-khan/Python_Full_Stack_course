# This Exercise will store only the Even numbers in list.
numbers=[1,1,2,3,5,8,13,21,34,55]
even_list=[num for num in numbers if num%2==0] # List comprhension.
print(even_list)