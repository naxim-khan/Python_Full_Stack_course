weather_c={
    "Monday":12,
    "Tuesday":14,
    "Wednesday":15,
    "Thursday":14,
    "Friday":21,
    "Saturday":22,
    "Sunday":24,
}
""" The above dictionary contents Days temperature in celsius 
convert the day temprature to Fahrenhit """

result={day:(temp*9/5)+32 for  (day,temp) in weather_c.items() }

print(result)