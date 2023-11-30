import random #random number module 
random_int1=random.randint(1,10)
random_int2=random.randint(1,10)
head=random_int1
tail=random_int2
if head>tail:
    print("Head")
elif head<tail:
    print("Tail")
