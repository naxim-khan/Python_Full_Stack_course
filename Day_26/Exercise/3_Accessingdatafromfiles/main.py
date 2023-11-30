# Instructions:
# Take a look inside file1.txt and file2.txt. they each contain 
# a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the 
# number's that are common both file.
file_1=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_26\\Exercise\\3_Accessingdatafromfiles\\file_1.txt")
file_2=("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_26\\Exercise\\3_Accessingdatafromfiles\\file_2.txt")
def file_reader(file):
    with open(file) as file:
        fileread=file.readlines()
        f=[int(i.replace("\n","")) for i in fileread]
        return f
    
file1=file_reader(file_1)
file2=file_reader(file_2)

result=[num for num in file1 if num in file2]

print(result)