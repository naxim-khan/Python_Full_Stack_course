"""Problem: 
Task
The provided code stub reads and integer,n, from STDIN. For all non-negative integers , print .

Example

The list of non-negative integers that are less than n=3 is [0,1,2]  is . Print the square of each number on a separate line."""
n=int(input("Enter a number: "))
for i in range(0,n):
    print(i**2)