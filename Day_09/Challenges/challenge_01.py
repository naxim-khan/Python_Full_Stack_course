# Greeting Program

# You've access to a database of a student_scores in the format of a dictionary.
# the key's is student_scors are the names of the student's and the values are 
# their exam Scores.

# Write a program that converts their scores to grades. By the end of the your
# program. You should have a new ditionary called student_grades that should contain
# student names for keys and their grades for values. The final version of the student_grades dictionary will be checked.

student_scores={
    "Harry"   :81,
    "Ron"     :78,
    "Hermione":99,
    "Draco"   :74,
    "Neville" :62,
}
# ToDo-1: Create an empty dictionary called students_grades
student_grades={}
#ToDo-2: Write your code below to add the grades
length=len(student_scores)
for grade in student_scores :
    names=grade
    scores=student_scores[grade]
    student_grades=student_scores[grade]
    if scores>90:
        student_grades="Outstanding!"
    elif scores>80:
        student_grades="Exceeds Expectation"
    elif scores>70:
        student_grades="Acceptable"
    else:
        student_grades="Fail"
    print(names,scores,student_grades)
# student_grades=student_grades[grades]


