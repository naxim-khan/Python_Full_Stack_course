# Find the hieighest score of in the class
scores=input("Enter a list of student's score: ").split(", ")
for i in range(0,len(scores)):
    scores[i]=int(scores[i])

print("List of scores",scores)
max_value=0
for n in range(0,len(scores)):
    if scores[n]>max_value:
        max_value=scores[n]
    
print("The highest scores is: ",max_value)

# ______ OR ______
print(max(scores))