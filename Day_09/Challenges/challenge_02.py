# Instructions : You are going to write a program that adds to
# trave_log. You can see a travel_log which is a List that contains 
# 2 Dictionaries.
# Write a function that will work with the following line of code
# on line 21 to add the entry for Russia to the travel_log.

# Hints: 1. Look at the function call above to see what the name
# of the function should be.
# the inputs for the function are postional arguments. the 
# the order is very important.
# Feel free to choose your own parameter nems.
travel_log=[
    {"country":"France",
     "visits":12,
    "cities_visited":["Paris","Lille","Dijon"],

      },
    {
        "country":"Germany",
        "visits": 5,
        "cities_visited":["Berlin","Hamburg","Stuttgart"]
    },
    # we a list which contain's two dictionaries
]

# adding a new country to the list
def add_new_country(country_visited,time_visited,cities_visited):
    new_country={}
    new_country["country"]=country_visited
    new_country["visits"]=time_visited
    new_country["cities_visited"]=cities_visited
    travel_log.append(new_country)


add_new_country("Russia",2,["Moscow","Saint Petersburg"])
print(travel_log)