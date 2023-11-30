"""new_dict={new_key:new_value for item in list}
new_dict={new_key:new_value for (key,value) in dict.items() if test}

"""
names=['Alex','Beth','Caroline','Dave','Elanor','Freddie']
import random
students_score={student:random.randint(1,100) for student in names}
passed_students={student:score for (student,score) in students_score.items() if score >= 60}
print(students_score)
print(passed_students)