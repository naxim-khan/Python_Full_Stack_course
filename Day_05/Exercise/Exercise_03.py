# Sum all the number's from 1 - 100 and also find
# the sum of even number's from 1-100.
a=int(input("Enter a range: "))
a+=1
total=0
even=0

for number in range(1,a):
    total+=number
    if number%2==0:
        even+=number
print(f"Sum from 1-{a-1} ={total} \nSum of even Number's are: {even}")