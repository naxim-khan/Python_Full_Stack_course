import csv  # a library for csv files
import pandas  # a library to manage the data in csv files

datas=pandas.read_csv("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_25\\project_1\\weather-data.csv")
print(datas["temp"])  # quick intro to padas library
temperature=[]

with open("F:\\U-DEMY-COURSES\\My_programms\\2nd_file\\Day_25\\project_1\\weather-data.csv") as weather_data:
    data=csv.reader(weather_data)
    
    for row in data:
        # print(row[1]) # accessing temp data 
        if row[1]!="temp":
            temperature.append(int(row[1]))

print(temperature)
