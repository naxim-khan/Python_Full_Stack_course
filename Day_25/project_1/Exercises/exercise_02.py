# find the average of temperatures
import csv
import pandas
data=pandas.read_csv("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_25\\project_1\\weather-data.csv")
data_dict=data.to_dict()
# # print(data_dict)
# temp_list=data["temp"]
# temperatures=[]
# for temp in temp_list:
#     temperatures.append(temp)
#     average_temp=(sum(temperatures))/len(temperatures)
# print(f"average_temp = {average_temp:.2f}")

# finding average of temperature
average_temp=data.temp.mean()
print(f"Average Temp: {average_temp:.2f}")
# finding maximum temperature
maximum_temp=data.temp.max()
print(f"Max Temp: {maximum_temp}")

# Geting data in columns
conditions=data.condition
print(f"Conditions\n{conditions}")
# Getting data in rows
row_data=data[data.day=="Monday"] # giving the name of the first column
print(f"data in row\n{row_data}")
maximum_temp_row=data[data.temp==data.temp.max()]  # finding the high temperature day in the week
print(f"High temperature day in week are\n{maximum_temp_row}")

# Converting mondy temperature from Celsuis to farenhite

monday=data[data.day=="Monday"]
monday_temp=int(monday.temp)
monday_fahrenhiet=(monday_temp*9)/5+32
print(f"Monday Temperature in Fahrenheit\n{monday_fahrenhiet}")

# Creating dataframe from scratch
data_ditionary={
    "students":["Amy","James","Angela"],
    "scores":[76,56,65]
}
s_data=pandas.DataFrame(data_ditionary)
# converting data fram to csv file
data.to_csv("new_data.csv")
print(s_data)

 