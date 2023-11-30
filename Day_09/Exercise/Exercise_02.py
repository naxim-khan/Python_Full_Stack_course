# Nesting in Dictionaries.
capitals={
    "France": "Paris",
    "Germany":"Berlin",
}
# Nesting a List in a Dictionary
# Nesting Dictionary in a Dictionary
travel_log={
    "France":{"cities_visited":["Paris","Lille","Dijon"],"total_vists":12},
    "Germany":{"cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5}
    
} 

# print(travel_log["Germany"])
#Nesting Dictionary in a List
travel_log=[
    {"country":"France",
      "cities_visited":["Paris","Lille","Dijon"],"total_vists":12
      },
    {
        "country":"Germany",
        "cities_visited":["Berlin","Hamburg","Stuttgart"],"total_visits":5
    },
    # we a list which contain's two dictionaries
]
