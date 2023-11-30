# find the average height of student's
students_heights=input("Enter list of students Height: ").split(", ")
for i in range(0,len(students_heights)):
    students_heights[i]=int(students_heights[i])
print("List of students Height: ",students_heights)
total_height=0
for height in students_heights:
    total_height+=height
print("Average =",total_height)
